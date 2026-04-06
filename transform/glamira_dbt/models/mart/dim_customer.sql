-- models/mart/dim_customer.sql
-- Purpose: Build customer dimension from the summary staging table.
--          Grain: one row per unique customer (user_id_db).

{{
  config(
    materialized = 'table',
    tags = ['mart', 'dimension']
  )
}}

WITH source AS (
    SELECT
        customer_id,
        email_address,
        user_agent,
        device_id,
        resolution,
        utm_source,
        utm_medium,
        -- Latest record wins when deduplicating by customer_id
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY event_timestamp DESC
        ) AS rn
    FROM {{ ref('stg_glamira__summary') }}
    WHERE customer_id IS NOT NULL
)

SELECT customer_id,
       user_agent,
       device_id,
       email_address,
       resolution,
       utm_source,
       utm_medium
FROM source
WHERE rn = 1
