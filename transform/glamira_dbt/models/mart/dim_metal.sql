-- models/mart/dim_metal.sql
-- Purpose: Build metal dimension from flattened colour options (metal is a sub-attribute of colour).
--          Grain: one row per unique metal ID.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_metal_source AS (
    SELECT DISTINCT
        metal_id,
        metal_name
    FROM {{ ref('int_colour_options') }}
    WHERE metal_id IS NOT NULL
)

SELECT metal_id,
       metal_name
FROM dim_metal_source
