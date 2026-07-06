{% snapshot dim_customer_snapshot %}

{{
    config(
      target_schema='glamira_snapshots',
      unique_key='customer_id',
      strategy='check',
      check_cols=['email_address'],
    )
}}

-- NOTE: device_id, user_agent, resolution, utm_source, utm_medium were removed.
-- These are session/event-level attributes, NOT customer attributes.
-- Keeping them here would inflate SCD2 versions with non-customer changes.
-- Device info is now handled as degenerate dimensions in fact_sales_order.

WITH latest_customer_state AS (
    SELECT
        customer_id,
        email_address,
        event_timestamp
    FROM {{ ref('stg_glamira__summary') }}
    WHERE customer_id IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY event_timestamp DESC) = 1
)

SELECT * FROM latest_customer_state

{% endsnapshot %}
