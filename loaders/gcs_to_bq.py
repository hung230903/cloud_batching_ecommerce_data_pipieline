from datetime import datetime

from google.cloud import bigquery

from config.base import (
    BQ_PROJECT_ID,
    BQ_DATASET_ID,
    BQ_TABLE_IP2LOCATION,
    BQ_TABLE_SUMMARY,
    BQ_TABLE_PRODUCT_INFO,
    GCS_BUCKET_NAME,
    GCS_SUMMARY_FOLDER,
    GCS_IP2LOCATION_FOLDER,
    GCS_PRODUCT_INFO_FOLDER
)
from config.logger import setup_logger

logger = setup_logger(
    name="gcs_to_bq",
    log_folder="loaders",
    log_file="gcs_to_bq.log",
)


def load_parquet_from_gcs(client, bucket_name, source_prefix, table_id):
    """Load all Parquet files from a GCS prefix into a BigQuery table."""
    table_ref = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.{table_id}"

    # Load Job Configuration: PARQUET format and append new data
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        # In a real DWH (Landing/Raw zone), we always append new data
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        # Apply Time Partitioning by load date (_PARTITIONTIME) 
        # and automatically delete raw data after 30 days to optimize storage costs
        time_partitioning=bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            expiration_ms=30 * 24 * 60 * 60 * 1000, # 30 days
        ),
    )

    uri = f"gs://{bucket_name}/{source_prefix}/*.parquet"

    logger.info(f"--- Loading data from {uri} to {table_ref} ---")

    try:
        load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
        load_job.result()  # Wait for the job to complete

        logger.info(f"SUCCESS: Loaded {load_job.output_rows} rows into {table_ref}.")
    except Exception as e:
        logger.error(f"FAILED to load BigQuery: {e}")
        raise


def run_load():
    start_time = datetime.now()
    logger.info(f"Starting BQ Load Job at {start_time}")

    client = bigquery.Client(project=BQ_PROJECT_ID)

    # Summary
    load_parquet_from_gcs(client, GCS_BUCKET_NAME, GCS_SUMMARY_FOLDER, BQ_TABLE_SUMMARY)

    # IP Location
    load_parquet_from_gcs(client, GCS_BUCKET_NAME, GCS_IP2LOCATION_FOLDER, BQ_TABLE_IP2LOCATION)

    # Product Info
    load_parquet_from_gcs(client, GCS_BUCKET_NAME, GCS_PRODUCT_INFO_FOLDER, BQ_TABLE_PRODUCT_INFO)

    end_time = datetime.now()
    logger.info(f"Finished BQ Load Job. Duration: {end_time - start_time}")


if __name__ == "__main__":
    # Remove local credentials if running in an environment with ADC
    # os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)

    run_load()
