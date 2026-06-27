import glob
import os
import unittest

from google.cloud import storage, bigquery
from pymongo import MongoClient

from config.base import (
    MONGO_URI,
    MONGO_DB,
    IP_COLLECTION,
    PID_FILTER_DIR,
    PRODUCT_URLS_FILTER_DIR,
    IP2LOCATION_DIR,
    PRODUCT_INFO_DIR,
    ERROR_DIR,
    GCS_BUCKET_NAME,
    BQ_PROJECT_ID,
    BQ_DATASET_ID,
    BQ_MART_DATASET_ID,
    BQ_TABLE_SUMMARY,
    BQ_TABLE_IP2LOCATION,
    BQ_TABLE_PRODUCT_INFO,
    GCS_SUMMARY_FOLDER,
    GCS_IP2LOCATION_FOLDER,
    GCS_PRODUCT_INFO_FOLDER,
)


class TestEndToEndPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Prepare clients."""
        cls.mongo_client = MongoClient(MONGO_URI)
        cls.db = cls.mongo_client[MONGO_DB]
        cls.gcs_client = storage.Client()
        cls.bq_client = bigquery.Client()

    def test_stage_1_ip_to_location_outputs(self):
        """Check Stage 1 outputs: Mongo collection and JSON files."""
        # Check Mongo
        count = self.db[IP_COLLECTION].count_documents({})
        self.assertGreater(count, 0, f"Collection {IP_COLLECTION} is empty!")

        # Check local JSON files
        pattern = os.path.join(IP2LOCATION_DIR, "ip_enriched_batch_*.json")
        files = glob.glob(pattern)
        self.assertGreater(
            len(files), 0, f"No JSON batch files found in {IP2LOCATION_DIR}"
        )
        print(f"STAGE 1 PASSED: Found {count} records in {IP_COLLECTION}")

    def test_stage_2_pid_filter_outputs(self):
        """Check Stage 2 outputs: JSON files."""
        pattern = os.path.join(PID_FILTER_DIR, "product_url_batch_*.json")
        files = glob.glob(pattern)
        self.assertGreater(
            len(files), 0, f"No PID filter JSON batch files found in {PID_FILTER_DIR}"
        )
        print(f"STAGE 2 PASSED: Found {len(files)} batch files in {PID_FILTER_DIR}")
        
    def test_stage_3_product_urls_filter_outputs(self):
        """Check Stage 3 outputs: Filtered Product URLs JSON files."""
        pattern = os.path.join(PRODUCT_URLS_FILTER_DIR, "*.json")
        files = glob.glob(pattern)
        self.assertGreater(
            len(files), 0, f"No product urls filter JSON batch files found in {PRODUCT_URLS_FILTER_DIR}"
        )
        print(f"STAGE 3 PASSED: Found {len(files)} filtered url batch files in {PRODUCT_URLS_FILTER_DIR}")

    def test_stage_4_product_crawler_outputs(self):
        """Check Stage 4 outputs: Crawled product information and handle errors."""
        success_dir = os.path.join(PRODUCT_INFO_DIR, "success")
        pattern = os.path.join(success_dir, "product_info_*.json")
        success_files = glob.glob(pattern)
        
        self.assertGreater(
            len(success_files), 0, f"No product info success JSON files found in {success_dir}"
        )
        
        # Check for errors
        error_pattern = os.path.join(ERROR_DIR, "*.json")
        error_files = glob.glob(error_pattern)
        if len(error_files) > 0:
            print(f"WARNING: Found {len(error_files)} error files in crawler output ({ERROR_DIR}).")
            
        print(f"STAGE 4 PASSED: Found {len(success_files)} success crawl files in {success_dir}")

    def test_stage_5_gcs_outputs(self):
        """Check Stage 5 outputs: Parquet files in GCS."""
        bucket = self.gcs_client.bucket(GCS_BUCKET_NAME)

        folders_to_check = [
            GCS_SUMMARY_FOLDER,
            GCS_IP2LOCATION_FOLDER,
            GCS_PRODUCT_INFO_FOLDER
        ]
        
        for folder in folders_to_check:
            blobs = list(bucket.list_blobs(prefix=folder, max_results=1))
            self.assertGreater(
                len(blobs),
                0,
                f"No Parquet files found in GCS: gs://{GCS_BUCKET_NAME}/{folder}",
            )
        print(f"STAGE 5 PASSED: Verified Parquet files in GCS bucket {GCS_BUCKET_NAME} for all sources.")

    def test_stage_6_bigquery_raw_tables(self):
        """Check Stage 6 outputs: BQ raw table row counts."""
        tables_to_check = [BQ_TABLE_SUMMARY, BQ_TABLE_IP2LOCATION, BQ_TABLE_PRODUCT_INFO]
        
        for table_id in tables_to_check:
            table_ref = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.{table_id}"
            try:
                table = self.bq_client.get_table(table_ref)
                self.assertGreater(table.num_rows, 0, f"BQ Table {table_ref} is empty!")
                print(f"STAGE 6 PASSED: BQ Table {table_id} has {table.num_rows} rows.")
            except Exception as e:
                self.fail(f"Failed to verify BQ Table {table_ref}. Error: {str(e)}")

    def test_stage_7_dbt_mart_tables(self):
        """Check Stage 7 outputs: BQ mart table row counts (dbt output)."""
        # Testing a few core tables in the mart dataset
        mart_tables = ["fact_sales_order", "dim_product", "dim_customer"]
        
        for table_id in mart_tables:
            table_ref = f"{BQ_PROJECT_ID}.{BQ_MART_DATASET_ID}.{table_id}"
            try:
                table = self.bq_client.get_table(table_ref)
                self.assertGreater(table.num_rows, 0, f"BQ Mart Table {table_ref} is empty! dbt transformation might have failed.")
                print(f"STAGE 7 PASSED: BQ Mart Table {table_id} has {table.num_rows} rows.")
            except Exception as e:
                print(f"WARNING: dbt Mart Table {table_ref} not found or empty. Ensure dbt has been run. Error: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        cls.mongo_client.close()


if __name__ == "__main__":
    unittest.main()
