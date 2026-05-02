-- models/intermediate/int_colour_options.sql
-- Purpose: Flatten the nested colour[] array from stg_glamira__product
--          into one row per colour+metal combination per product.
--          Feeds dim_colour and dim_metal in the mart layer.

WITH products AS (SELECT product_id,
                         colour
                  FROM {{ ref('stg_glamira__product') }}
                  WHERE colour IS NOT NULL),

     flattened AS (SELECT p.product_id,
                          c.element.option_id   AS colour_id,
                          c.element.option_type_id,
                          c.element.sku,
                          c.element.title       AS colour_name,
                          c.element.default_title,
                          c.element.price,
                          c.element.colour_code,
                          c.element.metal       AS metal_id,
                          c.element.metal_label AS metal_name,
                          c.element.colour_label

                   FROM products p,
                        UNNEST(p.colour.list) AS c)

SELECT *
FROM flattened
