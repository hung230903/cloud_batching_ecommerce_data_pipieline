import glob
import os
import unittest

from google.cloud import storage, bigquery
from pymongo import MongoClient

from config.base import (
    MONGO_URI, MONGO_DB, IP_COLLECTION,
    PID_FILTER_DIR, IP2LOCATION_DIR, PRODUCT_INFO_DIR,
    GCS_BUCKET_NAME, BQ_PROJECT_ID, BQ_DATASET_ID,
    BQ_TABLE_SUMMARY, BQ_TABLE_IP2LOCATION,
    GCS_SUMMARY_FOLDER, GCS_IP2LOCATION_FOLDER
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
        pattern = os.path.join(IP2LOCATION_DIR, "ip_location_batch_*.json")
        files = glob.glob(pattern)
        self.assertGreater(len(files), 0, f"No JSON batch files found in {IP2LOCATION_DIR}")
        print(f"STAGE 1 PASSED: Found {count} records in {IP_COLLECTION}")

    def test_stage_2_pid_filter_outputs(self):
        """Check Stage 2 outputs: JSON files."""
        pattern = os.path.join(PID_FILTER_DIR, "product_url_batch_*.json")
        files = glob.glob(pattern)
        self.assertGreater(len(files), 0, f"No PID filter JSON batch files found in {PID_FILTER_DIR}")
        print(f"STAGE 2 PASSED: Found {len(files)} batch files in {PID_FILTER_DIR}")

    def test_stage_3_product_crawler_outputs(self):
        """Check Stage 3 outputs: Crawford product information."""
        success_dir = os.path.join(PRODUCT_INFO_DIR, "success")
        pattern = os.path.join(success_dir, "product_info_*.json")
        files = glob.glob(pattern)
        # It's possible for some crawl jobs to fail, but for E2E we expect some success
        self.assertGreater(len(files), 0, f"No product info success JSON files found in {success_dir}")
        print(f"STAGE 3 PASSED: Found {len(files)} success crawl files in {success_dir}")

    def test_stage_4_gcs_outputs(self):
        """Check Stage 4 outputs: Parquet files in GCS."""
        bucket = self.gcs_client.bucket(GCS_BUCKET_NAME)

        # Check summary folder
        blobs = list(bucket.list_blobs(prefix=GCS_SUMMARY_FOLDER, max_results=1))
        self.assertGreater(len(blobs), 0, f"No Parquet files found in GCS: gs://{GCS_BUCKET_NAME}/{GCS_SUMMARY_FOLDER}")

        # Check ip2location folder
        blobs = list(bucket.list_blobs(prefix=GCS_IP2LOCATION_FOLDER, max_results=1))
        self.assertGreater(len(blobs), 0,
                           f"No Parquet files found in GCS: gs://{GCS_BUCKET_NAME}/{GCS_IP2LOCATION_FOLDER}")
        print(f"STAGE 4 PASSED: Verified Parquet files in GCS bucket {GCS_BUCKET_NAME}")

    def test_stage_5_bigquery_tables(self):
        """Check Stage 5 outputs: BQ table row counts."""
        for table_id in [BQ_TABLE_SUMMARY, BQ_TABLE_IP2LOCATION]:
            table_ref = f"{BQ_PROJECT_ID}.{BQ_DATASET_ID}.{table_id}"
            table = self.bq_client.get_table(table_ref)
            self.assertGreater(table.num_rows, 0, f"BQ Table {table_ref} is empty!")
            print(f"STAGE 5 PASSED: BQ Table {table_id} has {table.num_rows} rows.")

    @classmethod
    def tearDownClass(cls):
        cls.mongo_client.close()


if __name__ == "__main__":
    unittest.main()
