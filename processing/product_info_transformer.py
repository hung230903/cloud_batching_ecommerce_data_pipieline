import json
import pyarrow as pa
from schema.schemas import get_product_info_pyarrow_schema
from utils.data_transform_utils import safe_bool, safe_int, safe_float, safe_string

def _filter_dict_to_schema(data, schema_type):
    """
    Hàm đệ quy để lọc các field trong dict/list khớp với PyArrow Struct/List.
    PyArrow Struct rất nghiêm ngặt: không được thừa/thiếu field so với schema.
    """
    if data is None:
        return None

    # Nếu schema yêu cầu Struct
    if pa.types.is_struct(schema_type):
        if not isinstance(data, dict):
            return None
        filtered = {}
        for i in range(schema_type.num_fields):
            field = schema_type.field(i)
            val = data.get(field.name)
            filtered[field.name] = _filter_dict_to_schema(val, field.type)
        return filtered

    # Nếu schema yêu cầu List
    if pa.types.is_list(schema_type):
        if not isinstance(data, list):
            return []
        item_schema = schema_type.value_type
        return [_filter_dict_to_schema(item, item_schema) for item in data]

    # Kiểu dữ liệu nguyên tử (Scalar)
    if pa.types.is_integer(schema_type):
        return safe_int(data)
    if pa.types.is_floating(schema_type):
        return safe_float(data)
    if pa.types.is_boolean(schema_type):
        return safe_bool(data)
    if pa.types.is_string(schema_type):
        return safe_string(data)

    return data

def transform_product_info_data(df):
    """
    Tiến hành đệ quy và chuẩn hóa schema cho toàn bộ DataFrame
    """
    schema = get_product_info_pyarrow_schema()
    for name in schema.names:
        field_type = schema.field(name).type
        if name not in df.columns:
            df[name] = None
        
        df[name] = df[name].apply(lambda x: _filter_dict_to_schema(x, field_type))
    return df
