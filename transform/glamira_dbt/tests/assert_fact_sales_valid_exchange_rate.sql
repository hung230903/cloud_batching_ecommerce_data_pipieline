-- tests/assert_fact_sales_valid_exchange_rate.sql
-- Kiểm tra rằng exchange_rate_to_usd luôn dương và hợp lý (0 < rate <= 100).
-- Giá trị ngoài khoảng → có thể tỷ giá hardcode bị sai hoặc currency không nhận diện được.

SELECT
    sale_id,
    currency,
    exchange_rate_to_usd
FROM {{ ref('fact_sales_order') }}
WHERE exchange_rate_to_usd <= 0
   OR exchange_rate_to_usd > 100
