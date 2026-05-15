import os
import logging
from google.cloud import bigquery

# Cấu hình log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Các biến cấu hình lấy từ Environment Variables trên GCP Cloud Function
PROJECT_ID = os.getenv("BQ_PROJECT_ID")
DATASET_ID = os.getenv("BQ_DATASET_ID")
TABLE_SUMMARY = os.getenv("BQ_TABLE_SUMMARY")
TABLE_IP2LOCATION = os.getenv("BQ_TABLE_IP2LOCATION")
TABLE_PRODUCT_INFO = os.getenv("BQ_TABLE_PRODUCT_INFO")
SUMMARY_FOLDER = os.getenv("GCS_SUMMARY_FOLDER")
IP2LOCATION_FOLDER = os.getenv("GCS_IP2LOCATION_FOLDER")
PRODUCT_INFO_FOLDER = os.getenv("GCS_PRODUCT_INFO_FOLDER")

def trigger_bigquery_load(event, context):
    """
    Kích hoạt khi một file .parquet mới được upload lên GCS bucket.
    """
    file_path = event['name']
    bucket_name = event['bucket']
    
    # Chỉ xử lý file .parquet
    if not file_path.endswith('.parquet'):
        logger.info(f"Skipping non-parquet file: {file_path}")
        return

    logger.info(f"Detected new cloud file: gs://{bucket_name}/{file_path}")

    # 1. Xác định bảng đích dựa trên đường dẫn file
    if file_path.startswith(SUMMARY_FOLDER):
        table_id = TABLE_SUMMARY
    elif file_path.startswith(IP2LOCATION_FOLDER):
        table_id = TABLE_IP2LOCATION
    elif file_path.startswith(PRODUCT_INFO_FOLDER):
        table_id = TABLE_PRODUCT_INFO
    else:
        logger.warning(f"Unknown directory for file {file_path}. Skipping.")
        return

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{table_id}"
    client = bigquery.Client(project=PROJECT_ID)
    
    # 2. Cấu hình Load Job linh hoạt
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        # Sử dụng WRITE_APPEND vì đây là Cloud Function được kích hoạt theo thời gian thực (real-time)
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        # Cho phép BigQuery tự động thêm các field mới vào bảng nếu schema thay đổi
        schema_update_options=[
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
        ],
        # any schema changes will be automatically handled
        autodetect=False, 
    )

    uri = f"gs://{bucket_name}/{file_path}"
    
    try:
        logger.info(f"Starting BigQuery load job -> {table_ref}")
        load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
        load_job.result()  # Wait for the job to complete
        
        logger.info(f"SUCCESS: Loaded rows into {table_ref}")
    except Exception as e:
        logger.error(f"FAILED to load BigQuery: {e}")
        # Re-raise to let GCP see the failure
        raise e
