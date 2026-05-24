import os

from pymongo import MongoClient

from config.base import (
    IP2LOCATION_DIR,
    MONGO_DB,
    MONGO_URI,
    SUMMARY_COLLECTION,
    UNIQUE_IP_FILE,
)
from config.logger import setup_logger

logger = setup_logger(
    name="ip_unique_filter",
    log_folder="processing",
    log_file="uniques_ips",
)


def run_ip_unique_filter():

    client = MongoClient(MONGO_URI)

    try:
        db = client[MONGO_DB]
        summary_col = db[SUMMARY_COLLECTION]
        # output_col = db[IP_COLLECTION]
        # output_col.create_index("ip", unique=True)

        os.makedirs(IP2LOCATION_DIR, exist_ok=True)

        # Get IPs with batch=100k
        pipeline = [
            {"$match": {"ip": {"$nin": [None, "", "unknown", "127.0.0.1"]}}},
            {"$group": {"_id": "$ip"}},
        ]
        cursor = summary_col.aggregate(
            pipeline,
            allowDiskUse=True,
            batchSize=100_000,
        )

        # Write IPs for each batch to file
        ip_count = 0
        with open(UNIQUE_IP_FILE, "w", encoding="utf-8") as f:
            for doc in cursor:
                ip = doc.get("_id")
                if ip:
                    f.write(f"{ip}\n")
                    ip_count += 1

        logger.info(f" Extracted {ip_count} unique IPs to {UNIQUE_IP_FILE}")
        return ip_count
    finally:
        client.close()
        logger.info("PidFilter connection closed")


if __name__ == "__main__":
    run_ip_unique_filter()
