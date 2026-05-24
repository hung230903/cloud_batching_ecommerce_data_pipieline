-- models/intermediate/int_metal_translated.sql
-- Purpose: Deduplicate metal options and prioritize English names.

{{
  config(
    tags = ['intermediate', 'metal']
  )
}}

WITH dim_metal_source AS (
    SELECT
        metal_id,
        COALESCE(metal_name, 'Unknown') AS metal_name
    FROM {{ ref('int_colour_options') }}
    WHERE metal_id IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY metal_id
        ORDER BY
            CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') THEN 0 ELSE 1 END,
            store_code
    ) = 1
)

SELECT
    metal_id,
    metal_name
FROM dim_metal_source
