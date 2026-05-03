import os
import bson
from config.base import GCS_SUMMARY_FOLDER, MONGO_BATCH_SIZE, GCS_BUCKET_NAME
from config.logger import setup_logger
from processing.transformer.summary_transformer import transform_summary_data
from schema.schemas import get_summary_pyarrow_schema
from utils.checkpoint_utils import get_checkpoint_manager
from utils.gcs_upload_utils import _write_batch_to_gcs

logger = setup_logger(
    name="load_summary_to_gcs",
    log_folder="loaders",
    log_file="load_summary_to_gcs.log",
)

def export_bson_to_gcs(
        bson_file_path,
        collection_name,
        gcs_folder,
        transform_func=None,
        schema=None,
        batch_size=MONGO_BATCH_SIZE,
):
    """
    Đọc dữ liệu từ file BSON nội bộ theo batch,
    chuyển đổi sang Parquet và upload lên GCS.
    Hỗ trợ resume từ checkpoint sử dụng ObjectId.
    """
    checkpoint_manager = get_checkpoint_manager(f"data_to_gcs_{collection_name}")
    checkpoint_data = checkpoint_manager.get_checkpoint()

    last_id = None
    part_idx = 0

    if isinstance(checkpoint_data, dict):
        last_id = checkpoint_data.get("last_id")
        part_idx = checkpoint_data.get("part_idx", 0)
    elif isinstance(checkpoint_data, str):
        last_id = checkpoint_data

    logger.info(f"--- Processing BSON file: {bson_file_path} | Batch size: {batch_size:,} ---")
    if last_id:
        logger.info(
            f"[{collection_name}] Resuming from last_id: {last_id}, part_idx: {part_idx}. Scanning file... (This might take a moment)")

    current_batch = []
    processed = 0
    skip_mode = last_id is not None

    try:
        with open(bson_file_path, 'rb') as f:
            iterator = bson.decode_file_iter(f)
            for doc in iterator:
                doc_id = str(doc.get("_id"))

                if skip_mode:
                    if doc_id == last_id:
                        skip_mode = False
                        logger.info(f"[{collection_name}] Reached checkpoint last_id: {last_id}. Starting extraction.")
                    continue

                current_batch.append(doc)
                processed += 1

                if processed % 100000 == 0:
                    logger.info(f"[{collection_name}] Extracted: {processed:,} new records...")

                if len(current_batch) >= batch_size:
                    part_idx += 1
                    _write_batch_to_gcs(
                        current_batch, collection_name, gcs_folder,
                        part_idx, transform_func, schema, GCS_BUCKET_NAME
                    )

                    checkpoint_manager.save_checkpoint({
                        "last_id": str(current_batch[-1]["_id"]),
                        "part_idx": part_idx
                    })
                    current_batch = []

            if current_batch:
                part_idx += 1
                _write_batch_to_gcs(
                    current_batch, collection_name, gcs_folder,
                    part_idx, transform_func, schema, GCS_BUCKET_NAME
                )
                checkpoint_manager.save_checkpoint({
                    "last_id": str(current_batch[-1]["_id"]),
                    "part_idx": part_idx
                })

        logger.info(
            f"[{collection_name}] DONE | "
            f"Total NEW records exported: {processed:,} | "
            f"Total parts: {part_idx}"
        )
    except FileNotFoundError:
        logger.error(f"[{collection_name}] File not found: {bson_file_path}")
    except Exception as e:
        logger.error(f"[{collection_name}] Error reading BSON file: {e}")

def run_load_summary():
    logger.info("=== Exporting SUMMARY ===")
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bson_file_path = os.path.join(project_root, "data", "glamira-data", "summary.bson")

    summary_schema = get_summary_pyarrow_schema()
    export_bson_to_gcs(
        bson_file_path=bson_file_path,
        collection_name="summary",
        gcs_folder=GCS_SUMMARY_FOLDER,
        transform_func=transform_summary_data,
        schema=summary_schema,
    )

if __name__ == "__main__":
    run_load_summary()
