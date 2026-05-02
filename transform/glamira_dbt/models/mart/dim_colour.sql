-- models/mart/dim_colour.sql
-- Purpose: Build colour dimension from flattened colour options.
--          Grain: one row per unique colour option ID.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_colour_source AS (
    SELECT DISTINCT
        colour_id,
        colour_name
    FROM {{ ref('int_colour_options') }}
    WHERE colour_id IS NOT NULL
)

SELECT colour_id,
       colour_name
FROM dim_colour_source
