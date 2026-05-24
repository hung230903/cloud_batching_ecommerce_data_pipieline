-- models/mart/dim_product.sql
-- Purpose: Build the product dimension for business consumption.
--          Grain: one row per unique product.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

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
FROM {{ ref('int_product_translated') }}
WHERE product_name NOT IN ('Express Shipping', 'Shipping Label Fee')
