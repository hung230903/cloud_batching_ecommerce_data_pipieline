import logging

from config.base import CRAWLER_BATCH_SIZE
from extract.pid_filter import run_pid_filter
from extract.product_crawler import run_product_crawler
from loaders.gcs_to_bq import run_load as bq_load
from loaders.main_gcs_export import export_all
from loaders.mongo_loader.load_ip_to_mongo import run_ip_to_location as run_ip_transform

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def step_ip_to_location():
    logger.info("--- STAGE 1: IP TO LOCATION ---")
    run_ip_transform()


def step_pid_filter():
    logger.info("--- STAGE 2: PID FILTER ---")
    run_pid_filter()


def step_product_crawler():
    logger.info("--- STAGE 3: PRODUCT CRAWLER ---")
    run_product_crawler(batch_size=CRAWLER_BATCH_SIZE)


def step_export_to_gcs():
    logger.info("--- STAGE 4: EXPORT ALL TO GCS ---")
    export_all()


def step_bigquery_load():
    logger.info("--- OPTIONAL STAGE: BIGQUERY LOAD ---")
    bq_load()


def main():
    logger.info("=== STARTING FULL DATA PIPELINE FLOW ===")

    try:
        # Stage 1
        step_ip_to_location()

        # Stage 2
        step_pid_filter()

        # Stage 3
        step_product_crawler()

        # Stage 4
        step_export_to_gcs()

        # Optional Stage: Manually load data from gcs to bigquery
        # step_bigquery_load()

        logger.info("=== DATA PIPELINE COMPLETED SUCCESSFULLY ===")
    except Exception as e:
        logger.error(f"PIPELINE FAILED: {e}")


if __name__ == "__main__":
    main()
