-- models/intermediate/int_colour_translated.sql
-- Purpose: Deduplicate colour options and prioritize English colour names.

{{
  config(
    tags = ['intermediate', 'colour']
  )
}}

WITH english_colour_names AS (
    SELECT
        colour_code,
        colour_name AS english_name
    FROM {{ ref('int_colour_options') }}
    WHERE colour_code IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY colour_code
        ORDER BY CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') THEN 0 ELSE 1 END, store_code
    ) = 1
),

dim_colour_base AS (
    SELECT
        colour_id,
        colour_code,
        colour_name AS original_name
    FROM {{ ref('int_colour_options') }}
    WHERE colour_id IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY colour_id
        ORDER BY CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') THEN 0 ELSE 1 END, store_code
    ) = 1
)

SELECT
    b.colour_id,
    b.colour_code,
    COALESCE(e.english_name, b.original_name, 'Unknown') AS colour_name
FROM dim_colour_base b
LEFT JOIN english_colour_names e ON b.colour_code = e.colour_code
