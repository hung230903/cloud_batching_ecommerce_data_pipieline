-- models/intermediate/int_stone_translated.sql
-- Purpose: Deduplicate stone options and prioritize English names.

{{
  config(
    tags = ['intermediate', 'stone']
  )
}}

WITH english_stone_names AS (
    SELECT
        sku,
        title AS english_title
    FROM {{ ref('int_stone_options') }}
    WHERE sku IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY sku
        ORDER BY 
        CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') 
          THEN 0 
          ELSE 1 
        END, 
        store_code
    ) = 1
),

dim_stone_source AS (
    SELECT
        option_type_id AS stone_id,
        option_id,
        option_type_id,
        sku,
        title AS original_title,
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
            ORDER BY
                CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') 
                  THEN 0 
                  ELSE 1 
                END,
                store_code,
                product_id
        ) AS rn
    FROM {{ ref('int_stone_options') }}
    WHERE option_type_id IS NOT NULL
)

SELECT
    s.stone_id,
    s.option_id,
    s.option_type_id,
    s.sku,
    COALESCE(e.english_title, s.original_title, 'Unknown') AS title,
    s.default_title,
    s.price,
    configure_quality,
    s.stone_group,
    s.stone_type_default_label,
    s.stone_name_default_label,
    s.stone_certificate_default_label,
    s.carat_default_label,
    s.total_carat_default_label,
    s.diameter_default_label,
    s.shape_default_label,
    s.clarity_default_label,
    s.cut_default_label,
    s.color_default_label AS colour_default_label,
    s.origin_default_label,
    s.origin_color_default_label AS origin_colour_default_label,
    s.qty_default_label
FROM dim_stone_source s
LEFT JOIN english_stone_names e ON s.sku = e.sku
WHERE s.rn = 1
