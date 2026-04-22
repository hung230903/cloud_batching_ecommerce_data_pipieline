{% snapshot dim_customer_snapshot %}

{{
    config(
      target_schema='glamira_snapshots',
      unique_key='customer_id',
      strategy='timestamp',
      updated_at='event_timestamp',
    )
}}

WITH latest_customer_state AS (
    SELECT
        customer_id,
        email_address,
        user_agent,
        device_id,
        resolution,
        utm_source,
        utm_medium,
        event_timestamp
    FROM {{ ref('stg_glamira__summary') }}
    QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY event_timestamp DESC) = 1
)

SELECT * FROM latest_customer_state

{% endsnapshot %}
