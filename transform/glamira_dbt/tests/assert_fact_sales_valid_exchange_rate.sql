-- tests/assert_fact_sales_valid_exchange_rate.sql
-- Check that exchange_rate_to_usd is always positive and reasonable (0 < rate <= 100).
-- Values outside the range -> hardcoded exchange rate might be wrong or currency is not recognized.

SELECT
    sale_id,
    currency,
    exchange_rate_to_usd
FROM {{ ref('fact_sales_order') }}
WHERE exchange_rate_to_usd <= 0
   OR exchange_rate_to_usd > 100
