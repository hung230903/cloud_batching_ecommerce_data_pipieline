-- models/staging/stg_glamira__ip2location.sql
-- Purpose: Clean and cast the raw ip2location table.

WITH source AS (
    SELECT *
    FROM {{ source('glamira_raw', 'ip2location') }}
    QUALIFY ROW_NUMBER() OVER (PARTITION BY ip) = 1
),

renamed AS (
    SELECT
        ip AS ip_address,
        country AS country_long,
        country_short,
        region AS region_name,
        city AS city_name
    FROM source
)

SELECT *
FROM renamed
