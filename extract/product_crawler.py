import asyncio
import glob
import json
import os
import time
from urllib.parse import urlparse, parse_qs

import aiohttp

from config.base import (
    PID_FILTER_DIR,
    PRODUCT_INFO_DIR,
    CRAWLER_SEMAPHORE,
    CRAWLER_TIMEOUT,
    CRAWLER_MAX_RETRIES,
    CRAWLER_HEADERS,
    CRAWLER_BATCH_SIZE, CRAWLER_UA
)
from config.logger import setup_logger
from processing.enricher.product_info_enricher import extract_product_data
from utils.checkpoint_utils import get_checkpoint_manager
from utils.file_saving_utils import (
    save_success_data_to_files,
    save_error_data_to_files,
    save_exception_data_to_files,
)
from utils.time_utils import format_duration

# Module-level logger
logger = setup_logger(
    name="product_crawler",
    log_folder="extract",
    log_file="product_crawler.log",
)


def _get_ordered_urls(urls):
    valid_urls = []
    for u in urls:
        # Skip url if not string
        if not isinstance(u, str):
            continue
        # Check url if it http or https url
        parsed = urlparse(u)
        if parsed.scheme in ("http", "https"):
            valid_urls.append(u)

    def _score(url):
        # Evaluate urls
        parsed = urlparse(url)
        # Get number of params after '?' in url
        num_params = len(parse_qs(parsed.query))
        # Check the url if it contains 'stage'
        is_stage = 1 if "stage." in parsed.netloc else 0
        return is_stage, num_params, len(url)

    return sorted(valid_urls, key=_score)


def get_product_list_from_filter():
    pattern = os.path.join(PID_FILTER_DIR, "product_url_batch_*.json")
    files = sorted(glob.glob(pattern))

    products = []
    for f in files:
        with open(f, "r", encoding="utf-8") as f:
            products.extend(json.load(f))

    return products


async def get_product_info(session, product, initialized_domains, failed_domains, semaphore):
    # Get product id and urls
    pid = str(product["product_id"])
    candidate_urls = _get_ordered_urls(product["urls"])

    if not candidate_urls:
        return "invalid_url", {"pid": pid, "url": None, "all_urls": product.get("urls", [])}

    last_status = "failed"
    last_url_tried = None

    for url in candidate_urls:
        last_url_tried = url
        headers = CRAWLER_HEADERS.copy()
        headers["User-Agent"] = CRAWLER_UA
        domain = urlparse(url).netloc
        headers["Referer"] = f"https://{domain}/"

        # Skip if domain broken
        if domain in failed_domains:
            continue

        if domain not in initialized_domains:
            initialized_domains.add(domain)
            try:
                async with semaphore:
                    # Get Cookies from homepage for session for each domain
                    async with session.get(
                            f"https://{domain}/", headers=headers, allow_redirects=True, timeout=10
                    ) as home_resp:
                        await home_resp.text()
                        logger.info(f"Initialized session for domain: {domain}")
            except Exception as e:
                logger.warning(f"Failed to initialize domain {domain}: {e}")
                initialized_domains.discard(domain)
                # If initialize domains failed -> check it if 'dev', 'test, 'stage' -> ad to failed_domains
                if any(x in domain for x in ["dev", "test", "stage"]):
                    failed_domains.add(domain)
                continue

        for retry in range(1, CRAWLER_MAX_RETRIES + 1):
            try:
                async with semaphore:
                    async with session.get(url, headers=headers, allow_redirects=True) as response:
                        if response.status == 200:
                            html = await response.text()
                            product_data = extract_product_data(html)

                            if product_data:
                                logger.info(f"SUCCESS | ID: {pid} | URL: {url}")
                                return "success", product_data

                            status = "no_json_ld"
                            break  # Thử URL khác

                        status = response.status
                        if status == 403:
                            await asyncio.sleep(1 * retry)
                            break

                        if status >= 500 or status == 429:
                            await asyncio.sleep(1 * retry)
                        else:
                            break

            except asyncio.TimeoutError:
                status = "TimeoutError"
                await asyncio.sleep(0.5 * retry)
            except Exception as e:
                status = type(e).__name__
                break

        last_status = status

    return last_status, {"pid": pid, "url": last_url_tried, "all_urls": product.get("urls", [])}


async def _crawl_products_async(batch_size):
    start_time = time.perf_counter()

    products = get_product_list_from_filter()
    if not products:
        logger.error("FAILED | No products found from pid_filter. Run pid_filter first.")
        return

    success_products = []
    success_cnt = 0
    error_cnt = 0
    exception_cnt = 0

    # Checkpoint setup
    checkpoint_manager = get_checkpoint_manager("product_crawler")
    checkpoint_data = checkpoint_manager.get_checkpoint()

    start_index = 0
    file_idx = 1

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
        f"JOB START | CRAWLING {len(products)} products from Glamira PID Filter | Resuming from index {start_index}, file_idx {file_idx}")

    semaphore = asyncio.Semaphore(CRAWLER_SEMAPHORE)
    connector = aiohttp.TCPConnector(limit_per_host=CRAWLER_SEMAPHORE)
    timeout = aiohttp.ClientTimeout(total=CRAWLER_TIMEOUT)

    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        initialized_domains = set()
        failed_domains = set()

        for i in range(start_index, len(products), batch_size):
            batch = products[i: i + batch_size]
            tasks = [
                get_product_info(session, p, initialized_domains, failed_domains, semaphore)
                for p in batch
            ]

            for task in asyncio.as_completed(tasks):
                status, result = await task

                if status == "success":
                    success_products.append(result)
                    success_cnt += 1
                    if len(success_products) >= batch_size:
                        save_success_data_to_files(file_idx, success_products, logger)
                        success_products.clear()
                        file_idx += 1
                elif isinstance(status, int):  # HTTP status code for error
                    save_error_data_to_files(status, result, logger)  # result here is pid
                    error_cnt += 1
                else:  # Exception status (string)
                    save_exception_data_to_files(status, result, logger)  # result here is pid
                    exception_cnt += 1

            # Update checkpoint
            checkpoint_manager.save_checkpoint({
                "start_index": min(i + batch_size, len(products)),
                "file_idx": file_idx
            })

    if success_products:
        save_success_data_to_files(file_idx, success_products, logger)

    total_time = time.perf_counter() - start_time
    total_failed_products = error_cnt + exception_cnt
    logger.info(
        f"JOB END | SUCCESS: {success_cnt} | FAILED: {total_failed_products} "
        f"| ERROR: {error_cnt} | EXCEPTION: {exception_cnt} "
        f"| TIME: {format_duration(total_time)}"
    )


def run_product_crawler(batch_size=CRAWLER_BATCH_SIZE):
    asyncio.run(_crawl_products_async(batch_size))


if __name__ == "__main__":
    run_product_crawler()
