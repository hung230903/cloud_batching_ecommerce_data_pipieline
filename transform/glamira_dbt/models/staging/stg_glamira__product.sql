-- models/staging/stg_glamira__product.sql
-- Purpose: Clean the raw product_info table.
--          Keeps nested stone[] and colour[] arrays for downstream flattening.

WITH source AS (SELECT *
                FROM {{ source('glamira_raw', 'product_info') }}),

     renamed AS (SELECT
                     -- Identifiers
                     CAST(product_id AS STRING)      AS product_id,
                     product_name,
                     sku,
                     CAST(attribute_set_id AS INT64) AS attribute_set_id,
                     type_id,

                     -- Pricing
                     min_price,
                     max_price,

                     -- Classification
                     CAST(collection_id AS STRING)   AS collection_id,
                     CAST(category_id AS INT64)      AS category_id,
                     CAST(store_id AS STRING)        AS store_code,
                     gender,

                     -- Material attributes
                     material_design                 AS product_type_id,

                     -- Nested option arrays (used by transform layer)
                     stone,
                     colour,

                 FROM source)

SELECT *
FROM renamed
