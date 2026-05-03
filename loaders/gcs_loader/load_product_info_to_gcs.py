import glob
import json
import os

from config.base import (
    PRODUCT_INFO_DIR,
    GCS_BUCKET_NAME,
    GCS_DESTINATION_FOLDER
)
from config.logger import setup_logger
from schema.schemas import get_product_info_pyarrow_schema
from utils.gcs_upload_utils import _write_batch_to_gcs
from processing.transformer.product_info_transformer import transform_product_info_data

logger = setup_logger(
    name="load_product_to_gcs",
    log_folder="loaders",
    log_file="load_product_to_gcs.log",
)


def _get_product_json_files():
    """Lấy danh sách các tệp JSON thành công từ thư mục crawler."""
    success_dir = os.path.join(PRODUCT_INFO_DIR, "success")
    pattern = os.path.join(success_dir, "product_info_*.json")
    return sorted(glob.glob(pattern))


def run_load_product_to_gcs():
    """Đọc dữ liệu JSON, chuyển sang Parquet và đẩy lên GCS."""
    logger.info("=== Exporting PRODUCT INFO ===")

    from utils.checkpoint_utils import get_checkpoint_manager
    checkpoint_manager = get_checkpoint_manager("load_product_to_gcs")
    last_processed_file = checkpoint_manager.get_checkpoint()

    # Nếu checkpoint là dict (từ version mới), lấy ra file cuối
    if isinstance(last_processed_file, dict):
        last_processed_file = last_processed_file.get("last_file")

    json_files = _get_product_json_files()
    if not json_files:
        logger.warning("No product info JSON files found to upload.")
        return

    schema = get_product_info_pyarrow_schema()

    for i, file_path in enumerate(json_files, 1):
        filename = os.path.basename(file_path)

        # Bỏ qua các file đã xử lý
        if last_processed_file and filename <= last_processed_file:
            logger.info(f"Skipping already processed file: {filename}")
            continue

        logger.info(f"Processing file {i}/{len(json_files)}: {filename}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if not data:
                continue

            parquet_name = filename.replace(".json", ".parquet")
            
            _write_batch_to_gcs(
                batch=data,
                collection_name="product_info",
                gcs_folder=GCS_DESTINATION_FOLDER,
                part_idx=parquet_name,
                transform_func=transform_product_info_data,
                schema=schema,
                bucket_name=GCS_BUCKET_NAME
            )

            checkpoint_manager.save_checkpoint({"last_file": filename})

        except Exception as e:
            logger.error(f"ERROR | Failed to process {filename}: {e}")

    logger.info("JOB END | Finished Product Info export to GCS")


if __name__ == "__main__":
    run_load_product_to_gcs()

