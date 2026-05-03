import os
import sys
from datetime import datetime

# Add root path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from loaders.gcs_loader.load_product_info_to_gcs import run_load_product_to_gcs
from loaders.gcs_loader.load_summary_to_gcs import run_load_summary
from loaders.gcs_loader.load_ip2location_to_gcs import run_load_ip2location
from config.logger import setup_logger

logger = setup_logger(
    name="main_export",
    log_folder="loaders",
    log_file="export.log",
)


def export_all():
    # Gỡ bỏ credentials local để sử dụng ADC (Application Default Credentials) của GCP
    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)

    logger.info("=== STARTING DATA EXPORT PIPELINE ===")
    start_time = datetime.now()

    run_load_product_to_gcs()
    run_load_summary()
    run_load_ip2location()

    end_time = datetime.now()
    logger.info(f"=== PIPELINE FINISHED. Duration: {end_time - start_time} ===")


if __name__ == "__main__":
    export_all()
