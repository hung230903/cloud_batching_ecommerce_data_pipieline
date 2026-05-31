import os
import time
from concurrent.futures import ThreadPoolExecutor
from itertools import islice

from config.base import (
    IP2LOCATION_BATCH_SIZE,
    IP2LOCATION_DIR,
    UNIQUE_IP_FILE,
)
from config.logger import setup_logger
from extract.ip.ip_unique_filter import run_ip_unique_filter
from processing.enricher.ip_enricher import lookup_ip
from utils import time_utils
from utils.checkpoint_utils import get_checkpoint_manager
from utils.file_saving_utils import save_json_batch

logger = setup_logger(
    name="ip_to_location",
    log_folder="loaders",
    log_file="ip_to_location.log",
)


def _ip_generator(filepath, skip_count=0):
    """
    Use `islice` and `yield` for memory-efficient streaming.

    - `islice` lazily skips lines without loading the entire file into memory.
    - Avoids large RAM usage caused by `readlines()[skip_count:]`.
    - `yield` returns one IP at a time during iteration.
    - Designed for scalable checkpoint-based processing of large files.
    """

    # Yield IPs from text file, skipping the first `skip_count` IPs
    with open(filepath, "r", encoding="utf-8") as f:
        # islice func help to skip 'skip_count' IPs very fast
        for line in islice(f, skip_count, None):
            yield line.strip()


def _process_ips(checkpoint_manager, batch_size, workers):
    start = time.perf_counter()

    checkpoint_data = checkpoint_manager.get_checkpoint()

    checkpoint = 0
    file_idx = 1

    if isinstance(checkpoint_data, dict):
        checkpoint = checkpoint_data.get("ip_processed_count", 0)
        file_idx = checkpoint_data.get("file_idx", 1)
    elif isinstance(checkpoint_data, (str, int)):
        try:
            checkpoint = int(checkpoint_data)
            file_idx = (checkpoint // batch_size) + 1
        except (ValueError, TypeError):
            checkpoint = 0

    logger.info(
        f"Processing IPs from file (Skipping {checkpoint} IPs, start file_idx {file_idx})"
    )

    # Get IPs stream from text file
    ip_stream = _ip_generator(UNIQUE_IP_FILE, skip_count=checkpoint)

    # Initialize ThreadPoolExecutor to avoid Airflow daemonic process restriction
    with ThreadPoolExecutor(max_workers=workers) as executor:
        json_data = []
        ip_cnt = 0

        # Interate IPs from ip_stream to lookup_ip func
        for result in executor.map(lookup_ip, ip_stream, chunksize=1000):
            filename = f"ip_enriched_batch_{file_idx}.json"
            json_data.append(result)
            ip_cnt += 1

            if len(json_data) >= batch_size:
                save_json_batch(json_data, IP2LOCATION_DIR, filename, logger)

                # Update checkpoint
                checkpoint += len(json_data)
                checkpoint_manager.save_checkpoint(
                    {"ip_processed_count": checkpoint, "file_idx": file_idx + 1}
                )

                json_data.clear()
                file_idx += 1

        if json_data:
            filename = f"ip_enriched_batch_{file_idx}.json"
            save_json_batch(json_data, IP2LOCATION_DIR, filename, logger)
            checkpoint += len(json_data)
            checkpoint_manager.save_checkpoint(
                {"ip_processed_count": checkpoint, "file_idx": file_idx}
            )

    total_time = time.perf_counter() - start
    logger.info(
        f"Processed {ip_cnt} IPs | Time: {time_utils.format_duration(total_time)}"
    )
    return ip_cnt


def run_ip_enrichment(workers=10):
    """
    Execute the IP-to-location transformation pipeline.
    """
    start_time = time.perf_counter()
    logger.info("JOB START | Starting IP-to-location transformation")

    checkpoint_manager = get_checkpoint_manager("ip_to_location")
    checkpoint_data = checkpoint_manager.get_checkpoint()

    if isinstance(checkpoint_data, dict):
        checkpoint = checkpoint_data.get("ip_processed_count", 0)
    else:
        try:
            checkpoint = int(checkpoint_data or 0)
        except (ValueError, TypeError):
            checkpoint = 0

    # If checkpoint exists (> 0) -> skipped to preserve the order in file
    if checkpoint == 0:
        run_ip_unique_filter()
    elif not os.path.exists(UNIQUE_IP_FILE):
        logger.warning(
            "Checkpoint > 0 but extracted IPs file not found. Rebuilding file..."
        )
        run_ip_unique_filter()

    # Ensure the file has IPs to process
    if os.path.exists(UNIQUE_IP_FILE) and os.path.getsize(UNIQUE_IP_FILE) > 0:
        ip_cnt = _process_ips(checkpoint_manager, IP2LOCATION_BATCH_SIZE, workers)
    else:
        ip_cnt = 0
        logger.info("No IPs extracted, skipping.")

    total_time = time.perf_counter() - start_time
    total_time_formatted = time_utils.format_duration(total_time)
    logger.info(
        f"JOB END | IP-to-location complete | "
        f"Total IPs Transform: {ip_cnt} | Total Time: {total_time_formatted}"
    )


if __name__ == "__main__":
    run_ip_enrichment()
