-- models/mart/dim_customer.sql
-- Purpose: Building the Customer Dimension using SCD Type 2 tracking via dbt snapshots.
--          This table contains the full history of customer attribute changes.

{{
  config(
    materialized = 'table',
    tags = ['mart', 'dimension']
  )
}}

SELECT
    -- dbt Snapshot automatically adds:
    -- dbt_scd_id, dbt_updated_at, dbt_valid_from, dbt_valid_to
    *
FROM {{ ref('dim_customer_snapshot') }}
