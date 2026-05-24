import asyncio
import glob
import json
import os
import time
from urllib.parse import urlparse

import aiohttp

from config.base import (
    CRAWLER_BATCH_SIZE,
    CRAWLER_HEADERS,
    CRAWLER_MAX_RETRIES,
    CRAWLER_SEMAPHORE,
    CRAWLER_TIMEOUT,
    CRAWLER_UA,
    DOMAIN_MAX_REQUEST,
    ERROR_DIR,
    PRODUCT_INFO_DIR,
    PRODUCT_URLS_FILTER_DIR,
    SUCCESS_DIR,
)
from config.logger import setup_logger
from processing.enricher.product_info_enricher import extract_product_data
from processing.filter.product_urls_filter import run_url_filter
from utils.checkpoint_utils import get_checkpoint_manager
from utils.file_saving_utils import (
    save_json_batch,
    save_to_text_file,
)
from utils.time_utils import format_duration

logger = setup_logger(
    name="product_crawler",
    log_folder="extract",
    log_file="product_crawler.log",
)


# def save_failed_data(status, pid_info, logger, is_exception=False):
#     ERROR_DIR = os.path.join(PRODUCT_INFO_DIR, "error")
#     if isinstance(pid_info, dict):
#         pid = pid_info.get("pid")
#     else:
#         pid = pid_info

#     os.makedirs(ERROR_DIR, exist_ok=True)

#     # Save error pid to text file
#     with open(f"{ERROR_DIR}/{status}.txt", "a") as f:
#         f.write(f"{pid}\n")

#     if is_exception:
#         logger.error(f"FAILED | EXCEPTION | {status} | ID: {pid}")
#     else:
#         logger.error(f"FAILED | {status} | ID: {pid}")


def get_product_list_from_filter():
    pattern = os.path.join(PRODUCT_URLS_FILTER_DIR, "product_url_batch_*.json")
    files = sorted(glob.glob(pattern))

    products = []
    for f in files:
        with open(f, "r", encoding="utf-8") as file_content:
            products.extend(json.load(file_content))

    return products


async def get_product_info(
    session, product, initialized_domains, failed_domains, semaphore
):
    # Get product id and candidate urls (only get 15 urls)
    pid = str(product["product_id"])
    candidate_urls = product.get("urls", [])[:15]

    if not candidate_urls:
        return "invalid_url", {
            "pid": pid,
            "url": None,
            "all_urls": [],
        }

    last_status = "failed"
    last_url_tried = None
    status = "failed"

    for url in candidate_urls:
        """
        Initialize session cookie for domain.
        Some website need session cookie from homepage to access
        """

        last_url_tried = url
        headers = CRAWLER_HEADERS.copy()
        headers["User-Agent"] = CRAWLER_UA

        parsed = urlparse(url)
        domain = parsed.hostname
        headers["Referer"] = f"https://{domain}/"

        if not domain:
            continue

        if domain in failed_domains:
            status = "domain_failed"
            last_status = status
            continue

        if domain not in initialized_domains:
            initialized_domains.add(domain)
            try:
                async with semaphore:
                    async with session.get(
                        f"https://{domain}/",
                        headers=headers,
                        allow_redirects=True,
                        timeout=10,
                    ) as home_resp:
                        await home_resp.text()
                        logger.info(f"Initialized session for domain: {domain}")
            except Exception as e:
                # Remove that domain if failed and add to failed domains list
                logger.warning(f"Failed to initialize domain {domain}: {e}")
                initialized_domains.discard(domain)
                failed_domains.add(domain)
                status = "domain_init_failed"
                last_status = status
                continue

        for retry in range(1, CRAWLER_MAX_RETRIES + 1):
            """ Datat Crawl """
            try:
                async with semaphore:
                    async with session.get(
                        url, headers=headers, allow_redirects=True
                    ) as response:
                        if response.status == 200:
                            # Get all the html to extract data field
                            html = await response.text()
                            product_data = extract_product_data(html)

                            if product_data:
                                logger.info(f"SUCCESS | ID: {pid} | URL: {url}")
                                return "success", product_data

                            status = "no_json_ld"
                            logger.warning(
                                f"SKIP | ID: {pid} | Failed to extract product JSON-LD data from HTML for URL: {url}"
                            )
                            break

                        status = response.status
                        if status >= 500 or status == 429:
                            logger.warning(
                                f"RETRY {retry}/{CRAWLER_MAX_RETRIES} | ID: {pid} | HTTP status {status} for URL: {url}"
                            )
                            await asyncio.sleep(1 * retry)
                        else:
                            logger.warning(
                                f"SKIP | ID: {pid} | HTTP status {status} for URL: {url}"
                            )
                            break
            # Handle Retry if timeout or failed
            except asyncio.TimeoutError:
                status = "TimeoutError"
                logger.warning(
                    f"RETRY {retry}/{CRAWLER_MAX_RETRIES} | ID: {pid} | TimeoutError for URL: {url}"
                )
                await asyncio.sleep(0.5 * retry)
            except Exception as e:
                status = type(e).__name__
                logger.warning(
                    f"SKIP | ID: {pid} | Exception {status}: {e} for URL: {url}"
                )
                break

        last_status = status

    return last_status, {
        "pid": pid,
        "url": last_url_tried,
        "all_urls": candidate_urls,
    }


async def _crawl_products_async(batch_size):
    start_time = time.perf_counter()

    # Get product list after filter
    products = get_product_list_from_filter()
    if not products:
        logger.warning(
            "No products found from product urls filter files. Starting to run product_urls_filter."
        )
        run_url_filter()
        products = get_product_list_from_filter()  # Reload products after filtering

    success_products = []
    success_cnt = 0
    error_cnt = 0
    exception_cnt = 0

    checkpoint_manager = get_checkpoint_manager("product_crawler")
    checkpoint_data = checkpoint_manager.get_checkpoint()

    start_index = 0
    file_idx = 1
    success_filename = f"product_info_{file_idx}.json"

    # Set up checkpoint
    if isinstance(checkpoint_data, dict):
        start_index = checkpoint_data.get("start_index", 0)
        file_idx = checkpoint_data.get("file_idx", 1)
    elif isinstance(checkpoint_data, (str, int)):
        try:
            start_index = int(checkpoint_data)
        except (ValueError, TypeError):
            start_index = 0

    os.makedirs(PRODUCT_INFO_DIR, exist_ok=True)
    logger.info(
        f"JOB START | CRAWLING {len(products)} products | Resuming from index {start_index}, file_idx {file_idx}"
    )

    # Initialize timeout, semaphore and domain connector for session
    semaphore = asyncio.Semaphore(CRAWLER_SEMAPHORE)
    connector = aiohttp.TCPConnector(limit_per_host=DOMAIN_MAX_REQUEST)
    timeout = aiohttp.ClientTimeout(total=CRAWLER_TIMEOUT)

    # Initialize session for crawling
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        initialized_domains = set()
        failed_domains = set()
        total_products = len(products)
        processed_cnt = start_index

        for i in range(start_index, total_products, batch_size):
            # Set up product batch and tasks for crawling
            batch = products[i : i + batch_size]
            tasks = [
                get_product_info(
                    session,
                    p,
                    initialized_domains,
                    failed_domains,
                    semaphore,
                )
                for p in batch
            ]

            # Asyncio: as_completed yields tasks as they finish, without waiting for the entire batch
            for task in asyncio.as_completed(tasks):
                status, result = await task
                processed_cnt += 1
                percent = (processed_cnt / total_products) * 100
                error_filename = f"{status}.txt"

                # Categorize result: SUCCESS
                if status == "success":
                    success_products.append(result)
                    success_cnt += 1
                    # If the list reaches batch_size -> Write to JSON and clear the list for the next batch
                    if len(success_products) >= batch_size:
                        save_json_batch(
                            success_products,
                            SUCCESS_DIR,
                            success_filename,
                            logger,
                            message="SUCCESS | SAVED BATCH",
                            clean_data=True,
                        )
                        success_products.clear()
                        file_idx += 1

                # Categorize result: HTTP ERROR (e.g. 404, 500...)
                elif isinstance(status, int):
                    save_to_text_file(
                        result.get("pid"), ERROR_DIR, error_filename, logger, mode="a"
                    )
                    error_cnt += 1

                # Categorize result: SYSTEM/CODE ERROR (e.g. Timeout, invalid_url, Logic Exceptions...)
                else:
                    save_to_text_file(
                        result.get("pid"), ERROR_DIR, error_filename, logger, mode="a"
                    )
                    exception_cnt += 1

                # Log real-time progress for each product processed
                logger.info(
                    f"PROGRESS | {processed_cnt}/{total_products} ({percent:.2f}%) | "
                    f"Success: {success_cnt} | Fail/Err: {error_cnt + exception_cnt}"
                )

            # Save checkpoint
            checkpoint_manager.save_checkpoint(
                {
                    "start_index": min(i + batch_size, total_products),
                    "file_idx": file_idx,
                }
            )

    if success_products:
        save_json_batch(
            success_products,
            SUCCESS_DIR,
            success_filename,
            logger,
            message="SUCCESS | SAVED BATCH",
            clean_data=True,
        )
        checkpoint_manager.save_checkpoint(
            {
                "start_index": min(i + batch_size, total_products),
                "file_idx": file_idx,
            }
        )

    total_time = time.perf_counter() - start_time
    total_failed_products = error_cnt + exception_cnt
    logger.info(
        f"JOB END | SUCCESS: {success_cnt} | FAILED: {total_failed_products} "
        f"| ERROR: {error_cnt} | EXCEPTION: {exception_cnt} "
        f"| TIME: {format_duration(total_time)}"
    )


def run_product_crawler():
    asyncio.run(_crawl_products_async(CRAWLER_BATCH_SIZE))


if __name__ == "__main__":
    run_product_crawler()
