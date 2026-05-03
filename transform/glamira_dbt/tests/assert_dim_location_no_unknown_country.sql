-- tests/assert_dim_location_no_unknown_country.sql
-- Kiểm tra không có location nào với country_long bị rỗng hoặc chỉ là ký tự dash.
-- IP2Location trả về '-' khi không xác định được location.
-- Severity: warn (vì một số IP thực sự không thể resolve được)

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
