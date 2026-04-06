-- models/mart/dim_location.sql
-- Purpose: Build location dimension from ip2location staging.

{{
  config(
    materialized = 'table',
    tags = ['mart', 'dimension']
  )
}}

WITH source AS (
    SELECT DISTINCT
        ip_address,
        country_long,
        country_short,
        region_name,
        city_name
    FROM {{ ref('stg_glamira__ip2location') }}
    WHERE ip_address IS NOT NULL
)

SELECT
    -- Primary Key (natural key is the IP address)
    ip_address                   AS location_id,
    -- BigQuery stores IPs as strings; cast for compatibility
    FARM_FINGERPRINT(ip_address) AS ip_address_int,
    country_long,
    country_short,
    region_name,
    city_name
FROM source
