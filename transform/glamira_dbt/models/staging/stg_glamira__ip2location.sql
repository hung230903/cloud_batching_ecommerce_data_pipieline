-- models/staging/stg_glamira__ip2location.sql
-- Purpose: Clean and cast the raw ip2location table.

WITH source AS (SELECT *
                FROM {{ source('glamira_raw', 'ip2location') }}),

     renamed AS (SELECT ip                    AS ip_address,
                        country               AS country_long,
                        -- BigQuery ip2location schema uses country_long/short; map accordingly
                        SUBSTR(country, 1, 2) AS country_short,
                        region                AS region_name,
                        city                  AS city_name,
                        CAST(latitude AS FLOAT64)  AS latitude,
                        CAST(longitude AS FLOAT64) AS longitude
                 FROM source)

SELECT *
FROM renamed
