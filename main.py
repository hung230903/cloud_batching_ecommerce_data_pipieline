import logging
from config.base import CRAWLER_BATCH_SIZE
from extract.pid_filter import run_pid_filter
from extract.product_crawler import run_product_crawler
from loaders.load_ip_to_mongo import run_ip_to_location as run_ip_transform
from loaders.main_export import export_all
from loaders.gcs_to_bq import run_load as bq_load

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def step_ip_to_location():
    """BƯỚC 1: Chuyển đổi IP sang location và lưu vào MongoDB."""
    logger.info("--- STAGE 1: IP TO LOCATION ---")
    run_ip_transform()

def step_pid_filter():
    """BƯỚC 2: Lọc các Product ID và URL từ dữ liệu summary."""
    logger.info("--- STAGE 2: PID FILTER ---")
    run_pid_filter()

def step_product_crawler():
    """BƯỚC 3: Crawl thông tin sản phẩm từ các URL đã lọc."""
    logger.info("--- STAGE 3: PRODUCT CRAWLER ---")
    run_product_crawler(batch_size=CRAWLER_BATCH_SIZE)

def step_export_to_gcs():
    """BƯỚC 4: Export toàn bộ dữ liệu (Summary, IP2Location, Product Info) lên GCS."""
    logger.info("--- STAGE 4: EXPORT ALL TO GCS ---")
    export_all()

def step_bigquery_load():
    """BƯỚC 5: Nạp dữ liệu từ GCS vào BigQuery."""
    logger.info("--- STAGE 5: BIGQUERY LOAD ---")
    bq_load()

def main():
    """Điều phối toàn bộ flow của pipeline."""
    logger.info("=== STARTING FULL DATA PIPELINE FLOW ===")

    try:
        # 1. Làm giàu dữ liệu IP
        step_ip_to_location()

        # 2. Lọc PID
        step_pid_filter()

        # 3. Crawl dữ liệu sản phẩm mới
        step_product_crawler()

        # 4. Export toàn bộ dữ liệu lên GCS
        step_export_to_gcs()

        # 5. Manually load data from gcs to bigquery
        # step_bigquery_load()
        
        logger.info("=== DATA PIPELINE COMPLETED SUCCESSFULLY ===")
    except Exception as e:
        logger.error(f"PIPELINE FAILED: {e}")

if __name__ == "__main__":
    main()
