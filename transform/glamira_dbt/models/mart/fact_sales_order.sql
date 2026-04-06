-- models/mart/fact_sales_order.sql
-- Purpose: Transactional fact table for checkout_success events.
--          Grain: one row per product line in a successful order.
--
-- Foreign Keys:
--   product_id   -> dim_product.product_id
--   date_id      -> dim_date.date_id
--   location_id  -> dim_location.location_id  (= ip_address)
--   store_id     -> dim_store.store_id
--   stone_id     -> dim_stone.stone_id
--   colour_id    -> dim_colour.colour_id
--   metal_id     -> dim_metal.metal_id
--   user_id_db   -> dim_customer.customer_id

{{
  config(
    materialized = 'table',
    tags = ['mart', 'fact']
  )
}}

WITH checkout AS (
    SELECT *
    FROM {{ ref('int_checkout_events') }}
),

-- Join to dim_date to get the date_id surrogate key
with_date AS (
    SELECT
        c.*,
        d.date_id
    FROM checkout c
    LEFT JOIN {{ ref('dim_date') }} d
        ON CAST(FORMAT_DATE('%Y%m%d', DATE(c.event_timestamp)) AS INT64) = d.date_id
),

-- Normalize currency using static approximate exchange rates to USD
with_currency_exchange AS (
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
    FROM with_date
)

SELECT
    -- Primary Key
    sale_id,

    -- Degenerate / Natural Keys
    order_id,

    -- Foreign Keys
    date_id,
    local_time,
    ip_address              AS location_id,
    CAST(store_id AS INT64) AS store_id,
    product_id,

    -- Measures
    ROUND(amount, 2)                                  AS amount_raw,
    TRIM(currency)                                    AS currency,
    quantity,
    exchange_rate_to_usd,
    ROUND(amount * exchange_rate_to_usd, 2)           AS amount_usd,

    -- Option dimension keys
    stone_id,
    colour_id,
    metal_id,
    user_id_db

FROM with_currency_exchange
