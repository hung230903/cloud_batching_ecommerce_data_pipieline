-- macros/generate_schema_name.sql
-- Override dbt's default schema generation so that custom schemas
-- are used as-is (not prefixed with the target schema name).

{% macro generate_schema_name(custom_schema_name, node) -%}

    {%- set default_schema = target.schema -%}
    {%- if custom_schema_name is none -%}
        {{ default_schema }}
    {%- else -%}
        {{ custom_schema_name | trim }}
    {%- endif -%}

{%- endmacro %}
