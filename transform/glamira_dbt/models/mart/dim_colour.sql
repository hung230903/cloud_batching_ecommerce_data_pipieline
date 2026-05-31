-- models/mart/dim_colour.sql
-- Purpose: Build colour dimension.
--          Grain: one row per unique colour ID.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

SELECT
    colour_id,
    colour_code,
    colour_name,
    colour_label
FROM {{ ref('int_colour_translated') }}
