import os
from datetime import datetime

from config.logger import setup_logger
from loaders.gcs_loader.load_ip2location_to_gcs import run_load_ip2location
from loaders.gcs_loader.load_product_info_to_gcs import run_load_product_to_gcs
from loaders.gcs_loader.load_summary_to_gcs import run_load_summary

logger = setup_logger(
    name="main_export",
    log_folder="loaders",
    log_file="export.log",
)


def export_all():
    # Remove local credentials to use GCP's Application Default Credentials (ADC)
    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)

    logger.info("=== STARTING DATA EXPORT PIPELINE ===")
    start_time = datetime.now()

    run_load_ip2location()
    run_load_product_to_gcs()
    run_load_summary()

    end_time = datetime.now()
    logger.info(f"=== PIPELINE FINISHED. Duration: {end_time - start_time} ===")


if __name__ == "__main__":
    export_all()
