-- models/mart/dim_store.sql
-- Purpose: Build store dimension from distinct store_id values in the summary table.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_store_source AS (
    SELECT DISTINCT store_id
    FROM {{ ref('stg_glamira__summary') }}
    WHERE store_id IS NOT NULL
),

mapping AS (
    SELECT
        CAST(store_id AS STRING) AS store_id,
        store_code
    FROM {{ ref('dim_store_mapping') }}
)

SELECT
    s.store_id,
    COALESCE(m.store_code, 'Unknown') AS store_code
FROM dim_store_source AS s
LEFT JOIN mapping AS m ON s.store_id = m.store_id
