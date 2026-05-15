-- tests/assert_dim_product_has_name.sql
-- Check that every product in dim_product has a product_name.
-- Product without a name -> crawl might have failed or data is missing.

SELECT
    product_id,
    product_name
FROM {{ ref('dim_product') }}
WHERE product_name IS NULL
   OR TRIM(product_name) = ''
