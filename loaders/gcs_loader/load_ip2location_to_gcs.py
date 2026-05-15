import glob
import json
import os

from config.base import GCS_IP2LOCATION_FOLDER, IP2LOCATION_DIR, GCS_BUCKET_NAME
from config.logger import setup_logger
from processing.transformer.ip2location_transformer import transform_ip2location_data
from schema.schemas import get_ip2location_pyarrow_schema
from utils.checkpoint_utils import get_checkpoint_manager
from utils.gcs_upload_utils import write_batch_to_gcs

logger = setup_logger(
    name="load_ip2location_to_gcs",
    log_folder="loaders",
    log_file="load_ip2location_to_gcs.log",
)


def run_load_ip2location():
    """Read IP2Location data from JSON files and upload to GCS."""
    logger.info("=== Exporting IP2LOCATION ===")
    checkpoint_manager = get_checkpoint_manager("data_to_gcs_ip2location")
    last_processed_file = checkpoint_manager.get_checkpoint()

    pattern = os.path.join(IP2LOCATION_DIR, "ip_location_batch_*.json")
    json_files = sorted(glob.glob(pattern))

    if not json_files:
        logger.warning(f"No IP2Location JSON files found in {IP2LOCATION_DIR}.")
        return

    # If checkpoint is a dict (from new version), get the last file
    if isinstance(last_processed_file, dict):
        last_processed_file = last_processed_file.get("last_file")

    schema = get_ip2location_pyarrow_schema()

    for i, file_path in enumerate(json_files, 1):
        filename = os.path.basename(file_path)

        # Skip already processed files
        if last_processed_file and filename <= last_processed_file:
            logger.info(f"[ip2location] Skipping already processed file: {filename}")
            continue

        logger.info(f"[ip2location] Processing file {i}/{len(json_files)}: {filename}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if not data:
                continue

            parquet_name = filename.replace(".json", ".parquet")

            write_batch_to_gcs(
                batch=data,
                collection_name="ip2location",
                gcs_folder=GCS_IP2LOCATION_FOLDER,
                part_idx=parquet_name,
                transform_func=transform_ip2location_data,
                schema=schema,
                bucket_name=GCS_BUCKET_NAME
            )

            checkpoint_manager.save_checkpoint({"last_file": filename})

        except Exception as e:
            logger.error(f"[ip2location] Failed to process {filename}: {e}")


if __name__ == "__main__":
    run_load_ip2location()
