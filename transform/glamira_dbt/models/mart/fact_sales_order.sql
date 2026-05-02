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
        *,
        CASE TRIM(currency)
            WHEN '€' THEN 1.08
            WHEN '£' THEN 1.25
            WHEN 'kr' THEN 0.10
            WHEN '$' THEN 1.00
            WHEN 'USD $' THEN 1.00
            WHEN 'CHF' THEN 1.10
            WHEN 'AU $' THEN 0.65
            WHEN 'CAD $' THEN 0.74
            WHEN 'Kč' THEN 0.043
            WHEN 'Ft' THEN 0.0028
            WHEN 'zł' THEN 0.25
            WHEN 'MXN $' THEN 0.059
            WHEN 'SGD $' THEN 0.74
            WHEN 'CLP' THEN 0.0011
            WHEN 'лв.' THEN 0.55
            WHEN 'kn' THEN 0.14
            WHEN 'NZD $' THEN 0.60
            WHEN '₺' THEN 0.035
            WHEN 'COP $' THEN 0.00025
            WHEN 'PEN S/.' THEN 0.27
            WHEN '₱' THEN 0.018
            WHEN 'din.' THEN 0.009
            WHEN '₫' THEN 0.00004
            WHEN 'HKD $' THEN 0.13
            WHEN 'Lei' THEN 0.22
            WHEN 'GTQ Q' THEN 0.13
            WHEN 'CRC ₡' THEN 0.002
            WHEN '￥' THEN 0.0067
            WHEN '₹' THEN 0.012
            ELSE 1.00 -- Default fallback
        END AS exchange_rate_to_usd
    FROM fact_sales_order_with_location
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
    user_id_db

FROM fact_sales_order_with_currency
