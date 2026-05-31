import os
import time

from pymongo import MongoClient

from config.base import (
    MONGO_DB,
    MONGO_URI,
    PID_FILTER_BATCH_SIZE,
    PID_FILTER_DIR,
    PRODUCT_EVENT_COLLECTIONS,
    SUMMARY_COLLECTION,
)
from config.logger import setup_logger
from utils import time_utils
from utils.checkpoint_utils import get_checkpoint_manager
from utils.file_saving_utils import save_json_batch

logger = setup_logger(
    name="pid_filter",
    log_folder="extract",
    log_file="pid_filter.log",
)


def _build_pipeline(last_pid=None):
    """Build the aggregation pipeline.

    1. Match documents from product-related event collections.
    2. Project a unified product_id and url from varying field names.
    3. Filter out documents missing product_id or url.
    4. Group by (product_id, url) to get unique pairs.
    5. Sort by product_id so all URLs for the same product arrive
       consecutively — this allows streaming grouping in Python.
    """

    # Filter None value for product id and url
    match_stage = {
        "product_id": {"$ne": None},
        "url": {"$ne": None},
    }

    if last_pid is not None:
        match_stage["product_id"] = {"$gt": last_pid}

    return [
        {
            "$match": {
                "collection": {"$in": PRODUCT_EVENT_COLLECTIONS},
            }
        },
        {
            "$project": {
                "product_id": {
                    "$cond": [
                        {"$ne": ["$product_id", None]},
                        "$product_id",
                        "$viewing_product_id",
                    ]
                },
                "url": {
                    "$cond": [
                        {"$eq": ["$collection", "product_view_all_recommend_clicked"]},
                        "$referrer_url",
                        "$current_url",
                    ]
                },
            }
        },
        {"$match": match_stage},
        {
            "$group": {
                "_id": {
                    "product_id": "$product_id",
                    "url": "$url",
                }
            }
        },
        {"$sort": {"_id.product_id": 1}},
    ]


def _write_batch(batch, file_idx, output_dir, output_prefix):
    """Write a list of dicts to a numbered JSON file."""
    filename = f"{output_prefix}_{file_idx}.json"
    save_json_batch(data=batch, directory=output_dir, filename=filename, logger=logger)


def run_pid_filter(output_prefix="product_url_unique_batch"):
    """
    Execute the full extraction pipeline.
    MongoDB returns unique (product_id, url) pairs sorted by product_id.
    We stream through the cursor and group URLs per product_id in Python
    """

    start_time = time.perf_counter()
    logger.info("JOB START | Starting PID filter extraction")

    os.makedirs(PID_FILTER_DIR, exist_ok=True)

    client = MongoClient(MONGO_URI)
    try:
        db = client[MONGO_DB]
        collection = db[SUMMARY_COLLECTION]

        checkpoint_manager = get_checkpoint_manager("pid_filter")
        checkpoint_data = checkpoint_manager.get_checkpoint()

        last_pid = None
        file_counter = 1
        total_products = 0

        if isinstance(checkpoint_data, dict):
            last_pid = checkpoint_data.get("last_pid")
            file_counter = checkpoint_data.get("file_idx", 1)
            total_products = checkpoint_data.get("processed_count", 0)

        if total_products > 0:
            logger.info(
                f"Resuming from checkpoint | File idx: {file_counter} | Processed: {total_products}"
            )

        pipeline = _build_pipeline(last_pid=last_pid)
        cursor = collection.aggregate(
            pipeline,
            allowDiskUse=True,
            batchSize=10_000,
        )

        batch = []

        current_pid = None
        current_urls = []

        for doc in cursor:
            pid = doc["_id"]["product_id"]
            url = doc["_id"]["url"]

            if pid != current_pid:
                # Emit the previous product (if any)
                if current_pid is not None:
                    batch.append(
                        {
                            "product_id": current_pid,
                            "urls": current_urls,
                        }
                    )
                    total_products += 1

                    if len(batch) >= PID_FILTER_BATCH_SIZE:
                        _write_batch(batch, file_counter, PID_FILTER_DIR, output_prefix)

                        checkpoint_manager.save_checkpoint(
                            {
                                "last_pid": current_pid,
                                "file_idx": file_counter + 1,
                                "processed_count": total_products,
                            }
                        )

                        batch.clear()
                        file_counter += 1

                current_pid = pid
                current_urls = [url]
            else:
                current_urls.append(url)

        # Process the last product
        if current_pid is not None:
            batch.append(
                {
                    "product_id": current_pid,
                    "urls": current_urls,
                }
            )
            total_products += 1

        # Save remaining records
        if batch:
            _write_batch(batch, file_counter, PID_FILTER_DIR, output_prefix)
            checkpoint_manager.save_checkpoint(
                {
                    "last_pid": current_pid,
                    "file_idx": file_counter + 1,
                    "processed_count": total_products,
                }
            )

        total_time = time.perf_counter() - start_time
        total_time_formatted = time_utils.format_duration(total_time)
        logger.info(
            f"JOB END | PID filter extraction complete | "
            f"Total products: {total_products} | Total time: {total_time_formatted}"
        )
    finally:
        client.close()
        logger.info("PidFilter connection closed")


if __name__ == "__main__":
    run_pid_filter()
