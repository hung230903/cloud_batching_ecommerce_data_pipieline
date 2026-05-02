-- models/mart/dim_date.sql
-- Purpose: Generate a date dimension using a date spine from 2020-01-01 to 2030-12-31.
-- Follows the schema: dim_date

{{
  config(
    tags = ['mart', 'dimension']
  )
}}

WITH dim_date_spine AS (
    -- Generate one row per day using BigQuery GENERATE_DATE_ARRAY
    SELECT date_day
    FROM UNNEST(
        GENERATE_DATE_ARRAY(DATE '2020-01-01', DATE '2030-12-31', INTERVAL 1 DAY)
    ) AS date_day
)

SELECT
    -- Primary Key
    CAST(FORMAT_DATE('%Y%m%d', date_day) AS INT64) AS date_id,

    -- Descriptive attributes
    FORMAT_DATE('%Y-%m-%d', date_day)              AS full_date,
    FORMAT_DATE('%A', date_day)                    AS date_of_week,
    FORMAT_DATE('%a', date_day)                    AS date_of_week_short,
    CASE
        WHEN EXTRACT(DAYOFWEEK FROM date_day) IN (1, 7)
            THEN 'Weekend'
        ELSE 'Weekday'
        END                                        AS is_weekday_or_weekend,
    FORMAT_DATE('%d', date_day)                    AS day_of_month,
    DATE_TRUNC(date_day, MONTH)                    AS year_month,
    EXTRACT(DAYOFYEAR FROM date_day)               AS day_of_the_year,
    EXTRACT(WEEK FROM date_day)                    AS week_of_year,
    EXTRACT(QUARTER FROM date_day)                 AS quarter_number,
    EXTRACT(YEAR FROM date_day) AS year,
    EXTRACT(YEAR FROM date_day)                              AS year_number

FROM dim_date_spine
ORDER BY date_id
