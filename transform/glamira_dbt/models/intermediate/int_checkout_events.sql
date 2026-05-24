-- models/intermediate/int_checkout_events.sql
-- Purpose: Extract checkout_success events from staging summary.
--
-- IMPORTANT: In checkout_success events, product_id and price are ALWAYS NULL
-- at the top level. The actual order line items are nested inside cart_products[].
-- Each cart_products element contains: product_id, price, currency, amount, option[].
--
-- This model unnests cart_products to create one row per product line per order,
-- then extracts stone_id, colour_id, and metal_id from the nested option[] array
-- within each cart product.

WITH checkout AS (
    SELECT *
    FROM {{ ref('stg_glamira__summary') }}
    WHERE collection = 'checkout_success'
      AND order_id IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY event_timestamp DESC) = 1
),

-- Unnest cart_products to get one row per product line per order
cart_lines AS (
    SELECT
        c.order_id,
        c.customer_id AS user_id_db,
        c.device_id,
        c.user_agent,
        c.store_id,
        c.ip_address,
        c.event_timestamp,
        c.local_time,
        -- Extract product info from cart_products
        CAST(cp.element.product_id AS STRING) AS product_id,
        cp.element.price                      AS raw_price,
        cp.element.currency                   AS currency,
        cp.element.amount                     AS quantity,
        cp.element.option                     AS product_option,
        line_item_id
    FROM checkout c,
         UNNEST(c.cart_products.list) AS cp WITH OFFSET AS line_item_id
),

-- Parse the European formatted price string (e.g., "1.101,00") to a numeric value
priced AS (
    SELECT
        *,
        -- European format uses dots, spaces, or apostrophes as thousands sep, commas as decimal sep
        -- Use REGEXP_REPLACE to keep ONLY digits and the comma, then replace comma with period for FLOAT64
        CAST(
            NULLIF(REPLACE(REGEXP_REPLACE(raw_price, r'[^0-9,]', ''), ',', '.'), '') AS FLOAT64
        ) AS sale_price
    FROM cart_lines
),

-- Unnest the option array within cart_products and pivot stone/colour/metal
options_unnested AS (
    SELECT
        p.order_id,
        p.product_id,
        p.line_item_id,
        o.element.option_label,
        o.element.value_id,
        o.element.value_label
    FROM priced p,
         UNNEST(p.product_option.list) AS o
),

stone_options AS (
    SELECT o.order_id, o.line_item_id, o.product_id, o.value_id AS stone_id
    FROM options_unnested o
    JOIN {{ ref('int_stone_options') }} s ON o.value_id = s.option_type_id
    QUALIFY ROW_NUMBER() OVER (PARTITION BY o.order_id, o.line_item_id ORDER BY o.value_id) = 1
),

colour_options AS (
    SELECT o.order_id, o.line_item_id, o.product_id, o.value_id AS colour_id
    FROM options_unnested o
    JOIN {{ ref('int_colour_options') }} c ON o.value_id = c.option_type_id
    QUALIFY ROW_NUMBER() OVER (PARTITION BY o.order_id, o.line_item_id ORDER BY o.value_id) = 1
),

metal_options AS (
    SELECT o.order_id, o.line_item_id, o.product_id, c.metal_id AS metal_id
    FROM options_unnested o
    JOIN {{ ref('int_colour_options') }} c ON o.value_id = c.option_type_id
    WHERE c.metal_id IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (PARTITION BY o.order_id, o.line_item_id ORDER BY o.value_id) = 1
),

enriched AS (
    SELECT
        -- Generate a unique sale ID using store_id, order_id, and the line item position
        FARM_FINGERPRINT(
            CONCAT(
                COALESCE(p.store_id, ''),
                '|',
                COALESCE(p.order_id, ''),
                '|',
                CAST(p.line_item_id AS STRING)
            )
        ) AS sale_id,
        p.order_id,
        p.product_id,
        p.user_id_db,
        p.device_id,
        p.user_agent,
        p.store_id,
        p.ip_address,
        p.event_timestamp,
        p.local_time,

        -- Financials
        p.sale_price AS amount,
        p.currency,
        p.quantity,

        -- Resolved option IDs
        s.stone_id,
        col.colour_id,
        m.metal_id

    FROM priced p
    LEFT JOIN stone_options s
        ON p.order_id = s.order_id AND p.line_item_id = s.line_item_id
    LEFT JOIN colour_options col
        ON p.order_id = col.order_id AND p.line_item_id = col.line_item_id
    LEFT JOIN metal_options m
        ON p.order_id = m.order_id AND p.line_item_id = m.line_item_id
)

SELECT *
FROM enriched
