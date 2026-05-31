-- models/staging/stg_glamira__summary.sql
-- Purpose: Clean and type-cast the raw summary event table.
--          Selects only scalar (non-nested) fields needed for downstream models.

WITH source AS (
    SELECT *
    FROM {{ source('glamira_raw', 'summary') }}
),

renamed AS (
    SELECT
        CAST(order_id AS STRING) AS order_id,
        CAST(product_id AS STRING) AS product_id,
        CAST(store_id AS STRING) AS store_id,
        CAST(user_id_db AS STRING) AS customer_id,
        CAST(device_id AS STRING) AS device_id,
        collection,
        -- SAFE_CAST to TIMESTAMP fails; must convert via TIMESTAMP_SECONDS
        local_time,
        ip AS ip_address,
        email_address,
        user_agent,
        resolution,
        utm_source,
        utm_medium,
        referrer_url,
        price AS sale_price,
        currency,
        CAST(is_paypal AS BOOL) AS is_paypal,
        cart_products,
        option,
        -- time_stamp is Unix epoch seconds stored as string (e.g. "1590508488") -> convert to real time date/month/year...
        TIMESTAMP_SECONDS(CAST(time_stamp AS INT64)) AS event_timestamp
    FROM source
    WHERE time_stamp IS NOT NULL
)

SELECT *
FROM renamed
