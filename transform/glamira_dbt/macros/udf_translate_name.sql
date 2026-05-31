-- macros/udf_translate_name.sql
-- Purpose: Define a BigQuery JavaScript UDF that replaces ALL matching
--          translation keywords in a single pass (no multi-pass CTEs needed).
--          Longest keywords are matched first to avoid partial replacements.

{% macro udf_translate_name() %}

CREATE TEMP FUNCTION translate_name(
    name STRING,
    keywords ARRAY<STRING>,
    translations ARRAY<STRING>
)
RETURNS STRING
LANGUAGE js AS r"""
    if (!name || !keywords || !translations) return name;

    // Build pairs and sort by keyword length DESC (longest match first)
    let pairs = [];
    for (let i = 0; i < keywords.length; i++) {
        pairs.push({ keyword: keywords[i], translation: translations[i] });
    }
    pairs.sort((a, b) => b.keyword.length - a.keyword.length);

    // Apply all replacements in one pass
    let result = name;
    for (const p of pairs) {
        result = result.split(p.keyword).join(p.translation);
    }
    return result;
""";

{% endmacro %}
