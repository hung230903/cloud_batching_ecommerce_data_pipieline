{{
  config(
    materialized = 'table',
    tags = ['mart', 'dimension']
  )
}}

SELECT
    currency_code,
    exchange_rate_to_usd,
    currency_name
FROM {{ ref('exchange_rates') }}
