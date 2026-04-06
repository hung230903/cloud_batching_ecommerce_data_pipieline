-- models/mart/dim_product.sql
-- Purpose: Build the product dimension from the product_info staging table.
--          Grain: one row per unique product.

{{
  config(
    materialized = 'table',
    tags = ['mart', 'dimension']
  )
}}

WITH source AS (
    SELECT DISTINCT
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
        -- stone_id and metal_id/colour_id come from the first option in each array
        stone.list[SAFE_OFFSET(0)].element.option_id                 AS stone_id,
        colour.list[SAFE_OFFSET(0)].element.option_id                AS color_id,
        colour.list[SAFE_OFFSET(0)].element.metal                    AS metal_id,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            -- You can order by a timestamp if available; here we just pick any deterministic order
            ORDER BY sku
        ) AS rn
    FROM {{ ref('stg_glamira__product') }}
    WHERE product_id IS NOT NULL
)

SELECT product_id,
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
       stone_id,
       color_id,
       metal_id
FROM source
WHERE rn = 1
