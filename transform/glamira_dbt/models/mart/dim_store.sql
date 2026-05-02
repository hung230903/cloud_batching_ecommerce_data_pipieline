-- models/mart/dim_store.sql
-- Purpose: Build store dimension from distinct store_id values in the summary table.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_store_source AS (
    SELECT DISTINCT
        CAST(store_id AS INT64) AS store_id
    FROM {{ ref('stg_glamira__summary') }}
    WHERE store_id IS NOT NULL
)

SELECT store_id,
       -- store_name not available in raw data; use store_id as placeholder
       store_id AS store_name
FROM dim_store_source
