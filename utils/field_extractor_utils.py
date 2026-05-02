import json
import os
from collections import defaultdict


def get_type(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, dict):
        return "struct"
    elif isinstance(value, list):
        return "list"
    else:
        return "unknown"


def extract_schema(obj, path="", schema=None, counter=None):
    if schema is None:
        schema = defaultdict(set)
    if counter is None:
        counter = defaultdict(int)

    t = get_type(obj)

    if path:
        schema[path].add(t)
        counter[path] += 1

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{path}.{k}" if path else k
            extract_schema(v, new_path, schema, counter)

    elif isinstance(obj, list):
        for item in obj[:100]:  # sampling
            extract_schema(item, f"{path}[]", schema, counter)

    return schema, counter


def main():
    # Edit the file path to extract fields
    file_path = "../data/product_info/success/product_info_1.json"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    schema = defaultdict(set)
    counter = defaultdict(int)

    total_records = min(len(data), 500)

    for item in data[:total_records]:
        extract_schema(item, "", schema, counter)

    print("Schema: ")
    for path in sorted(schema.keys()):
        types = ", ".join(sorted(schema[path]))
        freq = counter[path]
        ratio = freq / total_records

        print(f"{path}: {types} | freq={freq}/{total_records} ({ratio:.2%})")


if __name__ == "__main__":
    main()
