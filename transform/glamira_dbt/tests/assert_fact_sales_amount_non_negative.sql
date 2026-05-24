-- tests/assert_fact_sales_amount_non_negative.sql
-- Check that all transaction amounts are >= 0.
-- If there are negative values -> error during price parsing or in source data.

SELECT
    sale_id,
    amount_raw,
    amount_usd
FROM {{ ref('fact_sales_order') }}
WHERE
    amount_raw < 0
    OR amount_usd < 0
