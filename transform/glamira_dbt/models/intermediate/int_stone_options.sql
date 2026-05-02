-- models/intermediate/int_stone_options.sql
-- Purpose: Flatten the nested stone[] array from stg_glamira__product
--          into one row per stone option per product.
--          This intermediate model feeds dim_stone in the mart layer.

WITH products AS (SELECT product_id,
                         stone
                  FROM {{ ref('stg_glamira__product') }}
                  WHERE stone IS NOT NULL),

     flattened AS (SELECT p.product_id,
                          s.element.option_id,
                          s.element.option_type_id,
                          s.element.sku,
                          s.element.title,
                          s.element.default_title,
                          s.element.price,
                          s.element.configure_quality,
                          s.element.stone_group,
                          -- Nested attribute extraction via safe field access
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.stone_type.default_label    AS stone_type_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.stone_name.default_label    AS stone_name_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.certificate.default_label   AS stone_certificate_default_label,
                          CAST(
                                  s.element.data_stones.list[SAFE_OFFSET(0)].element.carat.default_label AS FLOAT64
                          )                                                                              AS carat_default_label,
                          CAST(
                                  s.element.data_stones.list[SAFE_OFFSET(0)].element.total_carat.default_label AS FLOAT64
                          )                                                                              AS total_carat_default_label,
                          CAST(
                                  s.element.data_stones.list[SAFE_OFFSET(0)].element.diameter.default_label AS FLOAT64
                          )                                                                              AS diameter_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.shape.default_label         AS shape_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.clarity.default_label       AS clarity_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.cut.default_label           AS cut_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.colour.default_label        AS color_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.origin.default_label        AS origin_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.origin_colour.default_label AS origin_color_default_label,
                          s.element.data_stones.list[SAFE_OFFSET(0)].element.qty.default_label           AS qty_default_label

                   FROM products p,
                        UNNEST(p.stone.list) AS s)

SELECT *
FROM flattened
