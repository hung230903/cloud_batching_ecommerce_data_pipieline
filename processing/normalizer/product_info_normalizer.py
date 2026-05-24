import pyarrow as pa

from schema.schemas import get_product_info_pyarrow_schema
from utils.data_transform_utils import safe_bool, safe_float, safe_int, safe_string


def _filter_dict_to_schema(data, schema_type):
    """
    Recursive function to filter fields in dict/list to match PyArrow Struct/List.
    PyArrow Struct is extremely strict: no extra/missing fields allowed compared to the schema.
    """
    if data is None:
        return None

    # If schema requires a Struct
    if pa.types.is_struct(schema_type):
        if not isinstance(data, dict):
            return None
        filtered = {}
        for i in range(schema_type.num_fields):
            field = schema_type.field(i)
            val = data.get(field.name)
            filtered[field.name] = _filter_dict_to_schema(val, field.type)
        return filtered

    # If schema requires a List
    if pa.types.is_list(schema_type):
        if not isinstance(data, list):
            return []
        item_schema = schema_type.value_type
        return [_filter_dict_to_schema(item, item_schema) for item in data]

    # Atomic data type (Scalar)
    if pa.types.is_integer(schema_type):
        return safe_int(data)
    if pa.types.is_floating(schema_type):
        return safe_float(data)
    if pa.types.is_boolean(schema_type):
        return safe_bool(data)
    if pa.types.is_string(schema_type):
        return safe_string(data)

    return data


def normalize_product_info_data(df):
    """
    Recursively process and normalize schema for the entire DataFrame
    """
    schema = get_product_info_pyarrow_schema()
    for name in schema.names:
        field_type = schema.field(name).type
        if name not in df.columns:
            df[name] = None

        df[name] = df[name].apply(lambda x: _filter_dict_to_schema(x, field_type))
    return df
