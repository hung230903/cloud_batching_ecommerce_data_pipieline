-- models/mart/fact_sales_order.sql
-- Purpose: Transactional fact table for checkout_success events.
--          Grain: one row per product line in a successful order.
--
-- Foreign Keys:
--   product_id   -> dim_product.product_id
--   date_id      -> dim_date.date_id
--   location_id  -> dim_location.location_id
--   store_id     -> dim_store.store_id
--   stone_id     -> dim_stone.stone_id
--   colour_id    -> dim_colour.colour_id
--   metal_id     -> dim_metal.metal_id
--   user_id_db   -> dim_customer.customer_id

{{
  config(
    materialized = 'incremental',
    unique_key = 'sale_id',
    tags = ['mart', 'fact']
  )
}}

WITH fact_sales_order_checkout AS (
    SELECT *
    FROM {{ ref('int_checkout_events') }}
    {% if is_incremental() %}
    WHERE event_timestamp > (SELECT MAX(event_timestamp) FROM {{ this }})
    {% endif %}
),

-- Join to dim_date to get the date_id surrogate key
fact_sales_order_with_date AS (
    SELECT
        c.*,
        d.date_id
    FROM fact_sales_order_checkout c
    LEFT JOIN {{ ref('dim_date') }} d
        ON CAST(FORMAT_DATE('%Y%m%d', DATE(c.event_timestamp)) AS INT64) = d.date_id
),

-- Join to ip2location then dim_location to resolve location_id from ip_address
fact_sales_order_with_location AS (
    SELECT
        wd.*,
        loc.location_id
    FROM fact_sales_order_with_date wd
    LEFT JOIN {{ ref('stg_glamira__ip2location') }} ip2loc
        ON wd.ip_address = ip2loc.ip_address
    LEFT JOIN {{ ref('dim_location') }} loc
        ON loc.location_id = FARM_FINGERPRINT(
            CONCAT(
                COALESCE(ip2loc.country_long, ''),
                '|',
                COALESCE(ip2loc.region_name, ''),
                '|',
                COALESCE(ip2loc.city_name, '')
            )
        )
),

-- Normalize currency using static approximate exchange rates to USD
fact_sales_order_with_currency AS (
    SELECT
        f.*,
        COALESCE(c.exchange_rate_to_usd, 1.00) AS exchange_rate_to_usd
    FROM fact_sales_order_with_location f
    LEFT JOIN {{ ref('dim_currency') }} c
        ON TRIM(f.currency) = c.currency_code
)

SELECT
    -- Primary Key
    sale_id,

    -- Degenerate / Natural Keys
    order_id,

    -- Foreign Keys
    date_id,
    local_time,
    location_id,
    CAST(store_id AS INT64)                 AS store_id,
    product_id,

    -- Measures
    ROUND(amount, 2)                        AS amount_raw,
    TRIM(currency)                          AS currency,
    quantity,
    exchange_rate_to_usd,
    ROUND(amount * exchange_rate_to_usd, 2) AS amount_usd,

    -- Option dimension keys
    stone_id,
    colour_id,
    metal_id,
    user_id_db,

    -- Device info (degenerate dimensions — parsed from user_agent)
    device_id,
    CASE
        WHEN REGEXP_CONTAINS(LOWER(user_agent), r'(ipad|tablet|kindle|silk|playbook)')
            THEN 'Tablet'
        WHEN REGEXP_CONTAINS(LOWER(user_agent), r'(mobile|iphone|ipod|android.*mobile|opera\s*m)')
            THEN 'Mobile'
        ELSE 'Desktop'
    END                                     AS device_category,
    CASE
        WHEN REGEXP_CONTAINS(user_agent, r'Edg/')       THEN 'Edge'
        WHEN REGEXP_CONTAINS(user_agent, r'OPR/')        THEN 'Opera'
        WHEN REGEXP_CONTAINS(user_agent, r'Chrome/')     THEN 'Chrome'
        WHEN REGEXP_CONTAINS(user_agent, r'Safari/')
         AND NOT REGEXP_CONTAINS(user_agent, r'Chrome/') THEN 'Safari'
        WHEN REGEXP_CONTAINS(user_agent, r'Firefox/')    THEN 'Firefox'
        ELSE 'Other'
    END                                     AS browser_family,
    CASE
        WHEN REGEXP_CONTAINS(user_agent, r'Windows')     THEN 'Windows'
        WHEN REGEXP_CONTAINS(user_agent, r'Macintosh')   THEN 'macOS'
        WHEN REGEXP_CONTAINS(user_agent, r'iPhone|iPad') THEN 'iOS'
        WHEN REGEXP_CONTAINS(user_agent, r'Android')     THEN 'Android'
        WHEN REGEXP_CONTAINS(user_agent, r'Linux')       THEN 'Linux'
        ELSE 'Other'
    END                                     AS os_family

FROM fact_sales_order_with_currency

