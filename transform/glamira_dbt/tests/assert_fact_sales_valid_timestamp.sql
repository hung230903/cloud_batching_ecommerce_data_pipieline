-- tests/assert_fact_sales_valid_timestamp.sql
-- Kiểm tra rằng tất cả event_timestamp đều nằm trong khoảng hợp lý (2020–2030).
-- Nếu có giá trị ngoài khoảng → có lỗi trong quá trình chuyển đổi TIMESTAMP_SECONDS.

SELECT
    sale_id,
    order_id,
    event_timestamp
FROM {{ ref('int_checkout_events') }}
WHERE event_timestamp < TIMESTAMP('2020-01-01')
   OR event_timestamp > TIMESTAMP('2030-12-31')
