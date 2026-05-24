-- tests/assert_fact_sales_valid_timestamp.sql
-- Check that all event_timestamps fall within a reasonable range (2020-2030).
-- If values are outside this range -> error in TIMESTAMP_SECONDS conversion.

SELECT
    sale_id,
    order_id,
    event_timestamp
FROM {{ ref('int_checkout_events') }}
WHERE
    event_timestamp < TIMESTAMP('2020-01-01')
    OR event_timestamp > TIMESTAMP('2030-12-31')
