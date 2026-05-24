-- models/mart/dim_metal.sql
-- Purpose: Build metal dimension.
--          Grain: one row per unique metal ID.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

SELECT
    metal_id,
    metal_name
FROM {{ ref('int_metal_translated') }}
