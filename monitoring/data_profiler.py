import os
import sys
import pandas as pd
from pymongo import MongoClient
from google.cloud import bigquery
from datetime import datetime

# Add root path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.base import (
    MONGO_URI, MONGO_DB, SUMMARY_COLLECTION, IP_COLLECTION,
    BQ_PROJECT_ID, BQ_DATASET_ID, BQ_TABLE_SUMMARY, BQ_TABLE_IP2LOCATION,
    PRODUCT_INFO_DIR, BQ_TABLE_PRODUCT_INFO
)
import glob
import json
import random

# Tạo thư mục data_dictionary nếu chưa có
DICTIONARY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data_dictionary")
os.makedirs(DICTIONARY_DIR, exist_ok=True)

# Data Field Descriptions Dictionary (English)
FIELD_DESCRIPTIONS = {
    # Common Fields
    "product_id": "Unique identifier for the product",
    "product_name": "Full name of the product",
    "sku": "Stock Keeping Unit",
    "attribute_set_id": "ID of the product's attribute set",
    "attribute_set": "Name of the attribute set",
    "type_id": "Product type code",
    "min_price": "Formatted lowest possible price for the product",
    "max_price": "Formatted highest possible price for the product",
    "gold_weight": "Estimated gold weight of the metal part",
    "none_metal_weight": "Weight of the non-metal components",
    "fixed_silver_weight": "Fixed silver weight for silver items",
    "material_design": "Design code for the material/alloy",
    "collection": "Project collection name",
    "collection_id": "Unique ID of the collection",
    "product_type": "Broad product category",
    "product_type_value": "Internal identifier for the product type",
    "category_id": "Unique ID of the primary category",
    "category_name": "Display name of the category",
    "store_id": "Store or Country code",
    "gender": "Target gender",
    "media_image": "Product images container",
    "media_image.sku_image": "URL for the main SKU image",
    "media_video": "Product video container",
    "options": "Raw JSON configuration options containing all possible choices",
    "stone": "List of gemstone configurations currently assigned to the product",
    "stone.sku": "Gemstone unique SKU code",
    "stone.title": "Display name of the gemstone",
    "stone.price": "Additional price for selecting this stone",
    "stone.stone_quality": "Gemstone quality and attribute details",
    "stone.stone_quality.colour": "Gemstone color quality grade",
    "stone.stone_quality.clarity": "Gemstone clarity level",
    "stone.stone_quality.cut": "Gemstone cut quality",
    "stone.stone_quality.shape": "Gemstone shape",
    "stone.stone_group": "Classification of the stone",
    "colour": "Metal and Alloy configuration options",
    "color": "Alias for 'colour'",
    "colour.metal": "Metal material code",
    "colour.metal_label": "Display name of the metal material",
    "colour.colour_code": "Metal color code",
    "colour.price": "Price adjustment for this metal selection",
    "custom": "Miscellaneous custom options",
    "option": "User-selected product option in interaction events",
    "cart_products": "Array of products currently in the user's cart",
    "product_id_value": "Product ID value extracted for analytics",

    # Generic & Option Metadata Fields (Common in nested structures)
    "option_id": "Unique identifier for the product option configuration",
    "option_type_id": "Unique identifier for the specific value choice within an option",
    "is_default": "Boolean flag indicating if this is the standard/default selection",
    "price_type": "The logic used for price calculation (e.g., 'fixed', 'percent')",
    "store_title": "Localized display name of the option for the specific store view",
    "default_title": "Original/global title for the option or value",
    "is_require": "Boolean flag indicating if the option is mandatory for the product",
    "sort_order": "The numeric sequence for displaying options in the UI",
    "sku_image": "The image file suffix used for dynamic URL building based on SKU",

    # Summary Specific Fields
    "time_stamp": "Unix epoch timestamp of the event",

    "ip": "IP address of the user",
    "user_agent": "Browser and OS information of the user",
    "resolution": "Screen resolution of the device (Width x Height)",
    "user_id_db": "Internal database ID of the logged-in user",
    "device_id": "Unique persistent identifier for the user's device",
    "api_version": "Version of the tracking API",
    "local_time": "Literal local time captured from the user's device",
    "show_recommendation": "Boolean indicating if the recommendation block was visible",
    "current_url": "Full URL of the page where the event occurred",
    "referrer_url": "URL of the previous page that referred the user",
    "email_address": "User's email address if captured during the session",
    "recommendation": "Flag for recommendation-related interactions",
    "utm_source": "Marketing source identifier from the URL",
    "utm_medium": "Marketing medium identifier from the URL",
    "utm_campaign": "Marketing campaign name from the URL",
    "key_search": "Search keywords entered by the user",
    "price": "Price of the product during the event",
    "currency": "Currency code (e.g., EUR, USD, GBP)",
    "viewing_product_id": "ID of the product being viewed",
    "order_id": "ID of the sales order if applicable",
    "is_paypal": "Flag indicating if PayPal was selected or used",
    "recommendation_product_id": "ID of the product recommended to the user",
    "recommendation_product_position": "Index of the product in the recommendation list",
    "recommendation_clicked_position": "Position in the UI where the recommendation was clicked",

    # Nested Option Fields (Summary.option)
    "option.option_label": "Human-readable label for the product option (e.g., Metal, Size)",
    "option.option_id": "Technical identifier for the option type",
    "option.value_label": "Human-readable label for the selected value (e.g., Rose Gold, 52)",
    "option.value_id": "Technical identifier for the selected value",
    "option.quality": "Quality grade code for gems or materials",
    "option.quality_label": "Display name for the quality grade",
    "option.alloy": "Metal alloy specification",
    "option.diamond": "Diamond specification or grade",
    "option.shapediamond": "Shape of the diamond (e.g., Round, Princess)",
    "option.stone": "Type of gemstone selected",
    "option.pearlcolor": "Color of the pearl selected",
    "option.finish": "Surface finish type (e.g., Polished, Matte)",

    # IP2Location Fields
    "country": "Full name of the country",
    "region": "State, province, or region name",
    "city": "City name",
    "latitude": "Latitude coordinate of the IP location",
    "longitude": "Longitude coordinate of the IP location",

}

def _get_description(path):
    """Provides a detailed English description for a field path using direct map or pattern recognition."""
    p_lower = path.lower()
    
    # 1. Correct color/colour discrepancy
    normalized_path = path.replace("color.", "colour.").replace(".colour", ".colour_code")
    if p_lower == "color": normalized_path = "colour"
    
    # 2. Check direct map
    if normalized_path in FIELD_DESCRIPTIONS:
        return FIELD_DESCRIPTIONS[normalized_path]
    
    # 3. Fuzzy matching for components
    parts = normalized_path.split('.')
    leaf = parts[-1]
    
    # Rule based descriptions for common suffixes
    if leaf.endswith("_url"):
        return f"Web URL link to the resource: {leaf.replace('_url', '')}"
    if leaf.endswith("_label") or leaf.endswith("_title"):
        return f"Localized display name/label for the field: {leaf.split('_')[0]}"
    if leaf.endswith("_id") or leaf.endswith("_id_value"):
        return f"Internal system identifier for {leaf.replace('_id', '')}"
    if leaf.startswith("is_"):
        return f"Boolean flag/binary status: {leaf.replace('is_', '')}"
    if "price" in leaf:
        return "Monetary value or price-related setting"
    if "weight" in leaf:
        return "Physical weight value of a component"
    if leaf in ["pos", "position", "sort_order"]:
        return "Display sequence or sorting order"
    if leaf == "qty":
        return "Quantity or count of items"
    if leaf == "sku":
        return "Unique Stock Keeping Unit code"

    # Search in dictionary for the leaf name
    if leaf in FIELD_DESCRIPTIONS:
        return FIELD_DESCRIPTIONS[leaf]
        
    return "N/A (See parent components for context)"

def _df_to_markdown(df):
    """Xây dựng bảng Markdown thủ công từ DataFrame (không phụ thuộc 'tabulate')."""
    cols = df.columns
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        # Xử lý ký tự đặc biệt làm vỡ bảng MD
        row_clean = [str(v).replace("|", "\\|").replace("\n", " ").strip() for v in row]
        rows.append("| " + " | ".join(row_clean) + " |")
    return "\n".join([header, sep] + rows)

from config.logger import setup_logger
from config.logger import setup_logger

logger = setup_logger(
    name="data_profiler",
    log_folder="monitoring",
    log_file="profiler.log",
)

def _generate_deep_profile(data, source_name, custom_file_name=None):
    """
    Thực hiện profiling chuyên sâu và ghi kết quả ra file trong data_dictionary/.
    """
    if not data:
        logger.warning(f"{source_name} is empty.")
        return

    from collections import defaultdict
    # stats: lưu values (để đếm), types (để biết kiểu), samples (để ví dụ)
    field_stats = defaultdict(lambda: {"values": [], "types": set(), "samples": []})

    def walk(obj, prefix, is_list_item=False):
        # Tự động decode JSON strings
        if isinstance(obj, str) and obj.strip().startswith(('{', '[')):
            try:
                parsed = json.loads(obj)
                walk(parsed, prefix, is_list_item)
                return
            except:
                pass

        if prefix and not is_list_item:
            field_stats[prefix]["types"].add(type(obj).__name__)
            if isinstance(obj, (dict, list)):
                val_to_record = True if obj is not None and (not isinstance(obj, (dict, list)) or len(obj) > 0) else None
                field_stats[prefix]["values"].append(val_to_record)
            else:
                field_stats[prefix]["values"].append(obj)
                # Thu thập mẫu (tối đa 3 giá trị khác nhau)
                if obj is not None and len(field_stats[prefix]["samples"]) < 3:
                    if obj not in field_stats[prefix]["samples"]:
                        field_stats[prefix]["samples"].append(obj)

        if isinstance(obj, dict):
            for k, v in obj.items():
                walk(v, f"{prefix}.{k}" if prefix else k)
        elif isinstance(obj, list):
            for item in obj:
                walk(item, prefix, is_list_item=True)

    for doc in data:
        # Xử lý format của BigQuery row (nếu là Row object hoặc dict thô)
        if hasattr(doc, "items"): # dict-like
            walk(dict(doc), "")
        else:
            walk(doc, "")

    profile_summary = []
    for path, stats in field_stats.items():
        vals = stats["values"]
        non_null = [v for v in vals if v is not None and not (isinstance(v, float) and pd.isna(v))]
        null_count = len(vals) - len(non_null)
        
        try:
            distinct_count = len(set(non_null))
        except TypeError:
            distinct_count = len(set(str(v) for v in non_null))
        
        # Format sample string
        samples_str = ", ".join([str(s) for s in stats["samples"]])
        if not samples_str: samples_str = "N/A"

        profile_summary.append({
            "Field Path": path,
            "Types": ", ".join(sorted(stats["types"])),
            "Instances": len(vals),
            "Nulls": f"{null_count} ({(null_count/len(vals))*100 if vals else 0:.1f}%)",
            "Uniques": distinct_count,
            "Sample Data": samples_str,
            "Description": _get_description(path)
        })
        
    profile_df = pd.DataFrame(profile_summary).sort_values("Field Path")
    
    # Hiển thị ra console
    print(f"\n[{source_name} Deep Profiling Report]")
    with pd.option_context('display.max_rows', 10, 'display.max_columns', None):
        print(profile_df.to_string(index=False))

    # Ghi ra file Markdown
    if custom_file_name:
        file_path = os.path.join(DICTIONARY_DIR, custom_file_name)
    else:
        # Tên file cố định theo từng loại task
        lower_source = source_name.lower()
        if "product" in lower_source:
            task_key = "product_info"
        elif "summary" in lower_source:
            task_key = "summary_raw"
        else:
            task_key = source_name.replace(":", "_").replace(" ", "_").lower()
        file_path = os.path.join(DICTIONARY_DIR, f"{task_key}_data_dictionary.md")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Data Dictionary: {source_name}\n\n")
        f.write(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(_df_to_markdown(profile_df))
        f.write("\n\n---\n*Ghi chú: Bảng này được tạo tự động dựa trên mẫu dữ liệu hiện tại.*")
    
    logger.info(f"Saved Data Dictionary to: {file_path}")

def profile_mongodb_collection(mongo_uri, db_name, collection_name, sample_size=1000):
    """
    Profile a MongoDB collection with deep inspection.
    """
    logger.info(f"--- Profiling MongoDB Collection: {collection_name} (Sample: {sample_size}) ---")
    
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    
    # Check total count
    total_count = collection.count_documents({})
    logger.info(f"Total documents: {total_count:,}")
    
    # Check Indices
    indices = list(collection.list_indexes())
    print(f"\n[MongoDB: {collection_name} Constraints/Indices]")
    for idx in indices:
        print(f" - Index: {idx['name']} | Fields: {idx['key']} | Unique: {idx.get('unique', False)}")
    
    # Get sample data as list of dicts
    cursor = collection.find().limit(sample_size)
    data = list(cursor)
    
    # Loại bỏ _id khỏi profiling
    for d in data:
        if '_id' in d: del d['_id']
        
    _generate_deep_profile(data, f"MongoDB: {collection_name}")
    
    client.close()

def profile_local_product_info(product_info_dir):
    """
    Profile ONE random local JSON file for deep inspection (reads the entire file).
    """
    success_dir = os.path.join(product_info_dir, "success")
    json_files = glob.glob(os.path.join(success_dir, "product_info_*.json"))
    
    if not json_files:
        logger.warning(f"No product info JSON files found in {success_dir}")
        return
    
    selected_file = random.choice(json_files)
    logger.info(f"--- Profiling Local File: {os.path.basename(selected_file)} (Entire File) ---")
    
    try:
        with open(selected_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = [data]
            
            _generate_deep_profile(data, f"Local File: {os.path.basename(selected_file)}")
    except Exception as e:
        logger.error(f"Error reading file {selected_file}: {e}")

def profile_bigquery_table(client, dataset_id, table_id, sample_size=1000):
    """
    Profile a BigQuery table with deep inspection (including RECORD/STRUCT/ARRAY).
    """
    table_ref = f"{BQ_PROJECT_ID}.{dataset_id}.{table_id}"
    logger.info(f"--- Profiling BigQuery Table: {table_ref} (Sample: {sample_size}) ---")
    
    # 1. Get sample data (BigQuery auto-flattens Row objects slightly but we can cast to dict)
    query_sample = f"SELECT * FROM `{table_ref}` LIMIT {sample_size}"
    try:
        query_job = client.query(query_sample)
        results = query_job.result()
        data = [dict(row) for row in results]
    except Exception as e:
        logger.error(f"Failed to query BigQuery table {table_ref}: {e}")
        return

    if not data:
        logger.warning(f"No data found in BigQuery table {table_ref}.")
        return

    # Use the deep profiling logic to handle nested fields
    file_name = f"bq_{table_id}_profiler.md"
    _generate_deep_profile(data, f"BigQuery: {table_id}", custom_file_name=file_name)
    
    logger.info(f"Completed deep profiling for BigQuery table: {table_id}")

def run_profiling():
    logger.info("=== STARTING DATA PROFILING ===")
    
    # 1. Profile MongoDB
    logger.info("--- [1/3] MongoDB Collections Profiling ---")
    profile_mongodb_collection(MONGO_URI, MONGO_DB, SUMMARY_COLLECTION)
    profile_mongodb_collection(MONGO_URI, MONGO_DB, IP_COLLECTION)
    
    # 2. Profile Local Files
    logger.info("--- [2/3] Local JSON Files Profiling ---")
    profile_local_product_info(PRODUCT_INFO_DIR)
    
    # 3. Profile BigQuery
    logger.info("--- [3/3] BigQuery Tables Profiling ---")
    try:
        bq_client = bigquery.Client()
        profile_bigquery_table(bq_client, BQ_DATASET_ID, BQ_TABLE_SUMMARY)
        profile_bigquery_table(bq_client, BQ_DATASET_ID, BQ_TABLE_PRODUCT_INFO)
        profile_bigquery_table(bq_client, BQ_DATASET_ID, BQ_TABLE_IP2LOCATION)
    except Exception as e:
        logger.error(f"Failed to profile BigQuery: {e}")
        print(f"FAILED TO PROFILE BIGQUERY: {e}. Ensure you have GCP access.")

    logger.info("=== DATA PROFILING COMPLETED ===")

if __name__ == "__main__":
    run_profiling()
