-- models/mart/dim_stone.sql
-- Purpose: Build stone dimension.
--          Grain: one row per unique stone option.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

SELECT *
FROM {{ ref('int_stone_translated') }}
