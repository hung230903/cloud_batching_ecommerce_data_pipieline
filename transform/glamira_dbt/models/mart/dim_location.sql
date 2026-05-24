-- models/mart/dim_location.sql
-- Purpose: Build location dimension from ip2location staging.
--          Grain: one row per unique (country, region, city) combination.
--          Uses surrogate key to avoid IP-level duplication.

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_location_source AS (
    SELECT DISTINCT
        country_long,
        country_short,
        region_name,
        city_name
    FROM {{ ref('stg_glamira__ip2location') }}
    WHERE country_long IS NOT NULL
),

dim_location_surrogate AS (
    SELECT
        -- Surrogate key based on the unique combination of location attributes
        country_long,
        country_short,
        region_name,
        city_name,
        FARM_FINGERPRINT(
            CONCAT(
                COALESCE(country_long, ''),
                '|',
                COALESCE(region_name, ''),
                '|',
                COALESCE(city_name, '')
            )
        ) AS location_id
    FROM dim_location_source
)

SELECT *
FROM dim_location_surrogate
