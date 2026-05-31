-- models/intermediate/int_product_translated.sql
-- Purpose: Deduplicate products and apply translation/cleaning logic to product names.
--          Uses a JavaScript UDF to translate ALL keywords in a single pass
--          (replaces the previous multi-pass CTE approach).

{{
  config(
    tags = ['intermediate', 'product'],
    sql_header = udf_translate_name()
  )
}}

WITH english_product_names AS (
    SELECT
        sku,
        product_name AS english_name
    FROM {{ ref('stg_glamira__product') }}
    WHERE sku IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY sku
        ORDER BY CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') THEN 0 ELSE 1 END, store_code
    ) = 1
),

dim_product_source AS (
    SELECT
        product_id,
        product_name AS original_name,
        sku,
        attribute_set_id,
        type_id,
        min_price,
        max_price,
        collection_id,
        product_type_id,
        category_id,
        store_code,
        gender,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY
                CASE WHEN store_code IN ('glus', 'glgb', 'glau', 'glca') THEN 0 ELSE 1 END,
                store_code,
                sku
        ) AS rn
    FROM {{ ref('stg_glamira__product') }}
    WHERE product_id IS NOT NULL
),

dim_product_dedup_base AS (
    SELECT
        s.product_id,
        COALESCE(e.english_name, s.original_name) AS base_name,
        s.sku,
        s.attribute_set_id,
        s.type_id,
        s.min_price,
        s.max_price,
        s.collection_id,
        s.product_type_id,
        s.category_id,
        s.store_code,
        s.gender
    FROM dim_product_source s
    LEFT JOIN english_product_names e ON s.sku = e.sku
    WHERE s.rn = 1
),

-- Collect all translation keywords into arrays for the JS UDF
translation_arrays AS (
    SELECT
        -- Sort(DESC) all the records by original_keyword
        ARRAY_AGG(NORMALIZE(original_keyword, NFC) ORDER BY LENGTH(original_keyword) DESC) AS keywords,
        ARRAY_AGG(english_translation ORDER BY LENGTH(original_keyword) DESC) AS translations
    FROM {{ ref('product_category_translation') }}
),

-- Apply all translations in a single pass via JS UDF
dim_product_translated AS (
    SELECT
        b.product_id,
        translate_name(
            NORMALIZE(b.base_name, NFC),
            t.keywords,
            t.translations
        ) AS raw_product_name,
        b.sku,
        b.attribute_set_id,
        b.type_id,
        b.min_price,
        b.max_price,
        b.collection_id,
        b.product_type_id,
        b.category_id,
        b.store_code,
        b.gender
    FROM dim_product_dedup_base b
    CROSS JOIN translation_arrays t
)

SELECT
    product_id,
    REPLACE(
        REGEXP_REPLACE(
            REGEXP_REPLACE(
                REGEXP_REPLACE(
                    REGEXP_REPLACE(
                        REGEXP_REPLACE(
                            REPLACE(raw_product_name, 'Ø', ''),
                            r'\bRingAmazing\b', 'Ring Amazing'
                        ),
                        r'\bQuenn\b', 'Queen'
                    ),
                    r'\bFilirt\b', 'Flirt'
                ),
                r'\bExotic Ligh\b', 'Exotic Light'
            ),
            r'\bGracious love\b', 'Gracious Love'
        ),
        'GLAMIRA', 'Glamira'
    ) AS product_name,
    sku,
    attribute_set_id,
    type_id,
    min_price,
    max_price,
    collection_id,
    product_type_id,
    category_id,
    store_code,
    gender
FROM dim_product_translated
