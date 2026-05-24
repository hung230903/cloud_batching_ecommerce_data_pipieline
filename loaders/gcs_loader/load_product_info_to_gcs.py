import glob
import json
import os

from config.base import GCS_BUCKET_NAME, GCS_PRODUCT_INFO_FOLDER, SUCCESS_DIR
from config.logger import setup_logger
from processing.normalizer.product_info_normalizer import normalize_product_info_data
from schema.schemas import get_product_info_pyarrow_schema
from utils.checkpoint_utils import get_checkpoint_manager
from utils.gcs_upload_utils import write_batch_to_gcs

logger = setup_logger(
    name="load_product_to_gcs",
    log_folder="loaders",
    log_file="load_product_to_gcs.log",
)


def _get_product_json_files():
    """Get list of successful JSON files from the crawler directory."""
    pattern = os.path.join(SUCCESS_DIR, "*.json")
    return sorted(glob.glob(pattern))


def run_load_product_to_gcs():
    """Read JSON data, convert to Parquet, and upload to GCS."""
    logger.info("=== Exporting PRODUCT INFO ===")

    checkpoint_manager = get_checkpoint_manager("load_product_to_gcs")
    last_processed_file = checkpoint_manager.get_checkpoint()

    # If checkpoint is a dict (from new version), get the last file
    if isinstance(last_processed_file, dict):
        last_processed_file = last_processed_file.get("last_file")

    json_files = _get_product_json_files()
    if not json_files:
        logger.warning("No product info JSON files found to upload.")
        return

    schema = get_product_info_pyarrow_schema()

    for i, file_path in enumerate(json_files, 1):
        filename = os.path.basename(file_path)

        # Skip already processed files
        if last_processed_file and filename <= last_processed_file:
            logger.info(f"Skipping already processed file: {filename}")
            continue

        logger.info(f"Processing file {i}/{len(json_files)}: {filename}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not data:
                continue

            parquet_name = filename.replace(".json", ".parquet")

            write_batch_to_gcs(
                batch=data,
                collection_name="product_info",
                gcs_folder=GCS_PRODUCT_INFO_FOLDER,
                part_idx=parquet_name,
                transform_func=normalize_product_info_data,
                schema=schema,
                bucket_name=GCS_BUCKET_NAME,
            )

            checkpoint_manager.save_checkpoint({"last_file": filename})

        except Exception as e:
            logger.error(f"ERROR | Failed to process {filename}: {e}")

    logger.info("JOB END | Finished Product Info export to GCS")


if __name__ == "__main__":
    run_load_product_to_gcs()
