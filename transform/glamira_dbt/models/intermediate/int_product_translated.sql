-- models/intermediate/int_product_translated.sql
-- Purpose: Deduplicate products and apply translation/cleaning logic to product names.

{{
  config(
    tags = ['intermediate', 'product']
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

-- Pass 1: Apply longest-matching translation to base_name
translated_names_1 AS (
    SELECT
        b.product_id,
        REPLACE(
            NORMALIZE(b.base_name, NFC),
            NORMALIZE(t.original_keyword, NFC),
            t.english_translation
        ) AS translated_name,
        ROW_NUMBER() OVER (PARTITION BY b.product_id ORDER BY LENGTH(t.original_keyword) DESC) AS match_rank
    FROM dim_product_dedup_base b
    INNER JOIN {{ ref('product_category_translation') }} t
        ON NORMALIZE(b.base_name, NFC) LIKE CONCAT('%', NORMALIZE(t.original_keyword, NFC), '%')
),

-- Collect result after pass 1
after_pass1 AS (
    SELECT
        b.product_id,
        COALESCE(t1.translated_name, NORMALIZE(b.base_name, NFC)) AS name_after_pass1
    FROM dim_product_dedup_base b
    LEFT JOIN translated_names_1 t1 ON b.product_id = t1.product_id AND t1.match_rank = 1
),

-- Pass 2: Apply another round of translation to handle residual non-ASCII
translated_names_2 AS (
    SELECT
        a.product_id,
        REPLACE(
            a.name_after_pass1,
            NORMALIZE(t.original_keyword, NFC),
            t.english_translation
        ) AS translated_name,
        ROW_NUMBER() OVER (PARTITION BY a.product_id ORDER BY LENGTH(t.original_keyword) DESC) AS match_rank
    FROM after_pass1 a
    INNER JOIN {{ ref('product_category_translation') }} t
        ON a.name_after_pass1 LIKE CONCAT('%', NORMALIZE(t.original_keyword, NFC), '%')
),

dim_product_final AS (
    SELECT
        b.product_id,
        COALESCE(t2.translated_name, ap1.name_after_pass1) AS raw_product_name,
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
    LEFT JOIN after_pass1 ap1 ON b.product_id = ap1.product_id
    LEFT JOIN translated_names_2 t2 ON b.product_id = t2.product_id AND t2.match_rank = 1
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
FROM dim_product_final
