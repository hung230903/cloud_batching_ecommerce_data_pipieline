import json
import os
import time
from glob import glob

from pymongo import MongoClient, UpdateOne

from config.base import (
    IP2LOCATION_DIR,
    IP_COLLECTION,
    MONGO_DB,
    MONGO_URI,
)
from config.logger import setup_logger
from utils import time_utils
from utils.checkpoint_utils import get_checkpoint_manager

logger = setup_logger(
    name="load_enriched_ip_to_mongo",
    log_folder="loaders",
    log_file="load_enriched_ip_to_mongo.log",
)


def _get_file_index(filepath):
    filename = os.path.basename(filepath)
    try:
        # Expected filename: ip_location_batch_{idx}.json
        idx = int(filename.split("_")[-1].split(".")[0])
        return idx
    except (ValueError, IndexError):
        return 0


def load_enriched_ip_to_mongo():
    start_time = time.perf_counter()
    logger.info("JOB START | Starting loading enriched IPs to MongoDB")

    client = MongoClient(MONGO_URI)
    total_loaded = 0
    try:
        db = client[MONGO_DB]
        output_col = db[IP_COLLECTION]
        output_col.create_index("ip", unique=True)

        checkpoint_manager = get_checkpoint_manager("load_ip_to_mongo")
        checkpoint_data = checkpoint_manager.get_checkpoint()

        loaded_files = []
        if isinstance(checkpoint_data, list):
            loaded_files = set(checkpoint_data)
        elif isinstance(checkpoint_data, dict):
            loaded_files = set(checkpoint_data.get("loaded_files", []))
        else:
            loaded_files = set()

        # Find all json files in IP2LOCATION_DIR
        pattern = os.path.join(IP2LOCATION_DIR, "ip_enriched_batch_*.json")
        json_files = sorted(glob(pattern), key=_get_file_index)

        for file_path in json_files:
            filename = os.path.basename(file_path)
            if filename in loaded_files:
                continue

            # Read json data
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    json_data = json.load(f)
            except Exception as e:
                logger.error(f"Error reading file {filename}: {e}")
                continue

            if not json_data:
                loaded_files.add(filename)
                continue

            # Prepare bulk write
            mongo_batch = [
                UpdateOne(
                    {"ip": item["ip"]},
                    {"$set": item},
                    upsert=True,
                )
                for item in json_data
                if "ip" in item
            ]

            # Write data to mongo
            if mongo_batch:
                result = output_col.bulk_write(mongo_batch, ordered=False)
                logger.info(
                    f"File {filename} MongoDB completed: "
                    f"Processed {len(mongo_batch)} records | "
                    f"Upserted: {result.upserted_count}"
                )
                total_loaded += len(mongo_batch)

            # Update checkpoint
            loaded_files.add(filename)
            checkpoint_manager.save_checkpoint({"loaded_files": list(loaded_files)})

    finally:
        client.close()
        logger.info("MongoDB connection closed")

    total_time = time.perf_counter() - start_time
    total_time_formatted = time_utils.format_duration(total_time)
    logger.info(
        f"JOB END | Loading enriched IPs to MongoDB complete | "
        f"Total IPs Loaded: {total_loaded} | Total Time: {total_time_formatted}"
    )


if __name__ == "__main__":
    load_enriched_ip_to_mongo()
