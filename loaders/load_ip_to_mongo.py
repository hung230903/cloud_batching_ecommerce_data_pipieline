import os
import sys
import time
from pymongo import MongoClient, UpdateOne
from concurrent.futures import ProcessPoolExecutor
from itertools import islice

# Thêm root path để có thể import từ config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.base import (
    IP2LOCATION_DIR, IP2LOCATION_BATCH_SIZE,
    MONGO_URI, MONGO_DB, SUMMARY_COLLECTION, IP_COLLECTION
)
from config.logger import setup_logger
from utils import time_utils
from utils.file_saving_utils import save_json_batch
from processing.ip_transformer import lookup_ip
from utils.checkpoint_utils import get_checkpoint_manager

# Module-level logger
logger = setup_logger(
    name="ip_to_location",
    log_folder="loaders",
    log_file="ip_to_location.log",
)

UNIQUE_IPS_FILE = os.path.join(IP2LOCATION_DIR, "extracted_unique_ips.txt")


def _collect_unique_ips_to_file(summary_col):
    """Phase 1: Extract all unique IPs from MongoDB directly to a text file.
    
    This ensures a deterministic order for our checkpointing system.
    """
    phase1_start = time.perf_counter()
    logger.info("PHASE 1 START | Extracting unique IPs from MongoDB to file")

    os.makedirs(IP2LOCATION_DIR, exist_ok=True)

    pipeline = [{"$group": {"_id": "$ip"}}]
    cursor = summary_col.aggregate(
        pipeline,
        allowDiskUse=True,
        batchSize=100_000,
    )

    ip_count = 0
    with open(UNIQUE_IPS_FILE, "w", encoding="utf-8") as f:
        for doc in cursor:
            ip = doc.get("_id")
            if ip:
                f.write(f"{ip}\n")
                ip_count += 1

    phase1_time = time.perf_counter() - phase1_start
    logger.info(
        f"PHASE 1 END | Extracted {ip_count} unique IPs to {UNIQUE_IPS_FILE} | "
        f"Time: {time_utils.format_duration(phase1_time)}"
    )
    return ip_count


def _write_batch(output_col, mongo_batch, json_batch, file_idx):
    """Write a batch of results to MongoDB and a JSON file."""
    if not mongo_batch:
        return

    result = output_col.bulk_write(mongo_batch, ordered=False)
    logger.info(
        f"Batch {file_idx} MongoDB completed: "
        f"Processed {len(mongo_batch)} records | "
        f"Upserted: {result.upserted_count}"
    )

    filename = f"ip_location_batch_{file_idx}.json"
    save_json_batch(data=json_batch, directory=IP2LOCATION_DIR, filename=filename, logger=logger)


def _ip_generator(filepath, skip_count=0):
    """Yield IPs from the file, skipping the first `skip_count` IPs."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in islice(f, skip_count, None):
            yield line.strip()


def _process_ips(output_col, checkpoint_manager, batch_size, workers):
    """Phase 2: Process unique IPs from the flat file using multiprocessing."""
    phase2_start = time.perf_counter()

    checkpoint = int(checkpoint_manager.get_checkpoint() or 0)
    logger.info(f"PHASE 2 START | Processing IPs from file (Skipping {checkpoint} IPs)")

    # 1. Generator streaming from file
    ip_stream = _ip_generator(UNIQUE_IPS_FILE, skip_count=checkpoint)

    # 2. Process via ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=workers) as executor:
        mongo_data = []
        json_data = []
        ip_cnt = 0
        file_idx = (checkpoint // batch_size) + 1  # Offset file index based on checkpoint

        # executor.map consumes the generator efficiently with chunksize
        for result in executor.map(lookup_ip, ip_stream, chunksize=1000):
            mongo_data.append(
                UpdateOne(
                    {"ip": result["ip"]},
                    {"$set": result},
                    upsert=True,
                )
            )
            json_data.append(result)
            ip_cnt += 1

            if len(mongo_data) >= batch_size:
                _write_batch(output_col, mongo_data, json_data, file_idx)

                # Update checkpoint
                curr_ckpt = int(checkpoint_manager.get_checkpoint() or 0)
                checkpoint_manager.save_checkpoint(curr_ckpt + len(mongo_data))

                mongo_data.clear()
                json_data.clear()
                file_idx += 1

        if mongo_data:
            _write_batch(output_col, mongo_data, json_data, file_idx)
            curr_ckpt = int(checkpoint_manager.get_checkpoint() or 0)
            checkpoint_manager.save_checkpoint(curr_ckpt + len(mongo_data))

    phase2_time = time.perf_counter() - phase2_start
    logger.info(
        f"PHASE 2 END | Processed {ip_cnt} IPs | "
        f"Time: {time_utils.format_duration(phase2_time)}"
    )
    return ip_cnt


def run_ip_to_location(
        mongo_uri=MONGO_URI,
        mongo_db=MONGO_DB,
        raw_collection=SUMMARY_COLLECTION,
        ip_collection=IP_COLLECTION,
        batch_size=IP2LOCATION_BATCH_SIZE,
        workers=10,
):
    """Execute the IP-to-location transformation pipeline in two phases.
    
    Phase 1: Collect unique IPs to a flat file to ensure deterministic order.
    Phase 2: Stream IPs from the file, process them in multiprocessing mode.
    """
    start_time = time.perf_counter()
    logger.info("JOB START | Starting IP-to-location transformation")

    client = MongoClient(mongo_uri)
    try:
        db = client[mongo_db]
        summary_col = db[raw_collection]
        output_col = db[ip_collection]
        output_col.create_index("ip", unique=True)

        checkpoint_manager = get_checkpoint_manager("ip_to_location")
        checkpoint = int(checkpoint_manager.get_checkpoint() or 0)

        # Check if we should run Phase 1
        # If checkpoint exists (> 0), Phase 1 is skipped to preserve the order in file
        if checkpoint == 0:
            _collect_unique_ips_to_file(summary_col)
        elif not os.path.exists(UNIQUE_IPS_FILE):
            logger.warning("Checkpoint > 0 but extracted IPs file not found. Rebuilding file...")
            _collect_unique_ips_to_file(summary_col)

        # Ensure the file has IPs to process before moving to Phase 2
        if os.path.exists(UNIQUE_IPS_FILE) and os.path.getsize(UNIQUE_IPS_FILE) > 0:
            ip_cnt = _process_ips(output_col, checkpoint_manager, batch_size, workers)
        else:
            ip_cnt = 0
            logger.info("No IPs extracted, skipping Phase 2.")

    finally:
        client.close()
        logger.info("IpToLocation connection closed")

    total_time = time.perf_counter() - start_time
    total_time_formatted = time_utils.format_duration(total_time)
    logger.info(
        f"JOB END | IP-to-location transformation complete | "
        f"Total IPs Transform: {ip_cnt} | Total Time: {total_time_formatted}"
    )


if __name__ == "__main__":
    run_ip_to_location()
