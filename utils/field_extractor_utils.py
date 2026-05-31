import glob
import json
import os
from collections import defaultdict

import bson


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
        return type(value).__name__


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
        for item in obj:
            extract_schema(item, f"{path}[]", schema, counter)

    return schema, counter


def process_files(file_patterns, output_filename):
    schema = defaultdict(set)
    counter = defaultdict(int)
    total_records = 0

    all_files = []
    for pattern in file_patterns:
        all_files.extend(glob.glob(pattern))

    if not all_files:
        print(f"No files found for patterns: {file_patterns}")
        return

    print(f"Found {len(all_files)} files for {output_filename}. Starting scan...")

    for file_path in all_files:
        print(f"Scanning {file_path}...")
        if file_path.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            extract_schema(item, "", schema, counter)
                            total_records += 1
                    elif isinstance(data, dict):
                        extract_schema(data, "", schema, counter)
                        total_records += 1
                except Exception as e:
                    print(f"Error reading JSON {file_path}: {e}")

        elif file_path.endswith(".bson"):
            if bson is None:
                print("bson library not installed. Cannot process .bson files.")
                continue
            with open(file_path, "rb") as f:
                try:
                    for item in bson.decode_file_iter(f):
                        extract_schema(item, "", schema, counter)
                        total_records += 1
                        if total_records % 100000 == 0:
                            print(f"Scanned {total_records:,} BSON records...")
                except Exception as e:
                    print(f"Error reading BSON {file_path}: {e}")

    print(f"\n--- Scan Complete! Total records: {total_records:,} ---")

    # Save to file
    output_dir = "data/field_extractor"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Total records processed: {total_records:,}\n")
        f.write("Schema:\n\n")
        for path in sorted(schema.keys()):
            types = ", ".join(sorted(schema[path]))
            freq = counter[path]
            ratio = freq / total_records if total_records > 0 else 0
            f.write(f"{path}: {types} | freq={freq}/{total_records} ({ratio:.2%})\n")

    print(f"Saved extracted schema to: {output_path}\n")


def main():
    # Extract product info
    process_files(
        [
            "data/product_info/product_info_*.json",
            "data/product_info/success/product_info_*.json",
        ],
        "product_info_schema.txt",
    )

    # Extract summary
    process_files(["data/glamira-data/summary.bson"], "summary_schema.txt")


if __name__ == "__main__":
    main()
