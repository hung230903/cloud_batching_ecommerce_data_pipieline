import logging
import os

from google.cloud import bigquery

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration variables from Environment Variables on GCP Cloud Function
PROJECT_ID = os.getenv("BQ_PROJECT_ID", "your-gcp-project-id")
DATASET_ID = os.getenv("BQ_DATASET_ID", "raw_glamira_data")
TABLE_SUMMARY = os.getenv("BQ_TABLE_SUMMARY", "summary")
TABLE_IP2LOCATION = os.getenv("BQ_TABLE_IP2LOCATION", "raw_ip2location")
TABLE_PRODUCT_INFO = os.getenv("BQ_TABLE_PRODUCT_INFO", "product_info")
SUMMARY_FOLDER = os.getenv("GCS_SUMMARY_FOLDER", "summary_data")
IP2LOCATION_FOLDER = os.getenv("GCS_IP2LOCATION_FOLDER", "ip2location")
PRODUCT_INFO_FOLDER = os.getenv("GCS_PRODUCT_INFO_FOLDER", "product_info")


def trigger_bigquery_load(event, context):
    """
    Triggered when a new .parquet file is uploaded to the GCS bucket.
    """
    file_path = event.get("name")
    bucket_name = event.get("bucket")

    # Only process .parquet files
    if not file_path or not file_path.endswith(".parquet"):
        logger.info(f"Skipping non-parquet file: {file_path}")
        return

    logger.info(f"Detected new cloud file: gs://{bucket_name}/{file_path}")

    # 1. Determine target table based on file path
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

    # 2. Flexible Load Job configuration
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        create_disposition=bigquery.CreateDisposition.CREATE_IF_NEEDED,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        # Allow BigQuery to handle schema drift automatically
        schema_update_options=[
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
            bigquery.SchemaUpdateOption.ALLOW_FIELD_RELAXATION,
        ],
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
