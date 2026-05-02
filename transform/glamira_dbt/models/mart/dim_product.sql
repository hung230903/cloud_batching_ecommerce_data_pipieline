-- models/mart/dim_product.sql
-- Purpose: Build the product dimension from the product_info staging table.
--          Grain: one row per unique product.
--          NOTE: stone_id, color_id, metal_id removed — they are many-to-many
--          relationships handled via the bridge/fact tables.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_product_source AS (
    SELECT
        product_id,
        product_name,
        sku,
        attribute_set_id,
        type_id,
        min_price,
        max_price,
        collection_id,
        product_type_id,
        category_id,
        store_code,
        gender,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY sku
        ) AS rn
    FROM {{ ref('stg_glamira__product') }}
    WHERE product_id IS NOT NULL
),

dim_product_dedup AS (
    SELECT
        product_id,
        product_name,
        sku,
        attribute_set_id,
        type_id,
        min_price,
        max_price,
        collection_id,
        product_type_id,
        category_id,
        store_code,
        gender
    FROM dim_product_source
    WHERE rn = 1
)

SELECT *
FROM dim_product_dedup
