-- tests/assert_dim_location_no_unknown_country.sql
-- Check that no location has a country_long that is empty or just a dash character.
-- IP2Location returns '-' when the location cannot be determined.
-- Severity: warn (because some IPs truly cannot be resolved)

{{ config(severity='warn') }}

SELECT
    location_id,
    country_long,
    region_name,
    city_name
FROM {{ ref('dim_location') }}
WHERE country_long IS NULL
   OR TRIM(country_long) = ''
   OR TRIM(country_long) = '-'
