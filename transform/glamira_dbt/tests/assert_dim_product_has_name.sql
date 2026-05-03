-- tests/assert_dim_product_has_name.sql
-- Kiểm tra rằng mọi sản phẩm trong dim_product đều có product_name.
-- Product không có tên → có thể crawl failed hoặc data bị thiếu.

SELECT
    product_id,
    product_name
FROM {{ ref('dim_product') }}
WHERE product_name IS NULL
   OR TRIM(product_name) = ''
