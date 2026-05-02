-- models/mart/dim_stone.sql
-- Purpose: Build stone dimension from the flattened int_stone_options intermediate model.
--          Grain: one row per unique stone option (option_type_id is the PK).

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_stone_source AS (
    SELECT
        option_type_id                  AS stone_id,
        option_id,
        option_type_id,
        sku,
        title,
        default_title,
        price,
        configure_quality,
        stone_group,
        stone_type_default_label,
        stone_name_default_label,
        stone_certificate_default_label,
        carat_default_label,
        total_carat_default_label,
        diameter_default_label,
        shape_default_label,
        clarity_default_label,
        cut_default_label,
        color_default_label,
        origin_default_label,
        origin_color_default_label,
        qty_default_label,
        ROW_NUMBER() OVER (
            PARTITION BY option_type_id
            ORDER BY product_id
        ) AS rn
    FROM {{ ref('int_stone_options') }}
    WHERE option_type_id IS NOT NULL
),

dim_stone_dedup AS (
    SELECT
        stone_id,
        option_id,
        option_type_id,
        sku,
        title,
        default_title,
        price,
        configure_quality,
        stone_group,
        stone_type_default_label,
        stone_name_default_label,
        stone_certificate_default_label,
        carat_default_label,
        total_carat_default_label,
        diameter_default_label,
        shape_default_label,
        clarity_default_label,
        cut_default_label,
        color_default_label,
        origin_default_label,
        origin_color_default_label,
        qty_default_label
    FROM dim_stone_source
    WHERE rn = 1
)

SELECT *
FROM dim_stone_dedup
