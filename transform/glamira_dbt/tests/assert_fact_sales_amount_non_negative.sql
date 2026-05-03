-- tests/assert_fact_sales_amount_non_negative.sql
-- Kiểm tra rằng tất cả số tiền giao dịch đều >= 0.
-- Nếu có giá trị âm → có lỗi trong quá trình parse price hoặc dữ liệu nguồn.

SELECT
    sale_id,
    amount_raw,
    amount_usd
FROM {{ ref('fact_sales_order') }}
WHERE amount_raw < 0
   OR amount_usd < 0
