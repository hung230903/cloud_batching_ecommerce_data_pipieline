import glob
import json
import os
import re
from functools import lru_cache
from urllib.parse import parse_qsl, urlparse

from config.base import (
    DOMAINS_PATH,
    PID_FILTER_BATCH_SIZE,
    PID_FILTER_DIR,
    PRODUCT_URLS_FILTER_DIR,
)
from config.logger import setup_logger
from utils.file_saving_utils import save_json_batch, save_to_text_file

logger = setup_logger(
    name="product_domains_filter",
    log_folder="process",
    log_file="product_domains_filter.log",
)


def get_product_list():
    path = os.path.join(PID_FILTER_DIR, "product_url_batch_*.json")
    files = sorted(glob.glob(path))

    products = []
    for f in files:
        with open(f, "r", encoding="utf-8") as file_content:
            products.extend(json.load(file_content))

    return products


@lru_cache(maxsize=1)
def filter_domains():
    all_domains = set()
    allowed_domains = set()
    blocked_domains = set()

    blocked_pattern = re.compile(
        r"(^|\.)((dev\d*)|stage|test)\.|\.local$",
        re.IGNORECASE,
    )

    files = sorted(glob.glob(os.path.join(PID_FILTER_DIR, "product_url_batch_*.json")))

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

            for product in data:
                for url in product["urls"]:
                    parsed = urlparse(url)
                    domain_parsed = parsed.netloc.lower().rstrip(".")

                    if not domain_parsed:
                        continue

                    all_domains.add(domain_parsed)

                    is_allowed = (
                        "glamira" in domain_parsed or "ring-paare.de" in domain_parsed
                    )

                    if is_allowed and not blocked_pattern.search(domain_parsed):
                        allowed_domains.add(domain_parsed)
                    else:
                        blocked_domains.add(domain_parsed)

    return all_domains, blocked_domains, allowed_domains


def scored_url(urls):
    """
    filter and prioritize product urls.

    rules:
    1. keep only valid http/https urls
    2. prioritize urls:
       - with fewer query parameters
       - shorter urls
    """

    # Get allowed_domains
    _, _, allowed_domains = filter_domains()

    # get urls
    valid_urls = []
    for u in urls:
        # skip url if not string
        if not isinstance(u, str):
            continue

        # parse url
        parsed = urlparse(u)

        # Check domain: hostname cần được đưa về lowercase và strip trailing dot để đồng bộ
        domain = parsed.hostname.lower().rstrip(".") if parsed.hostname else None
        if not domain or domain not in allowed_domains:
            continue

        # check url if it http or https url
        if parsed.scheme not in ("http", "https"):
            continue

        valid_urls.append(u)

    def score(url):
        """
        compute priority score for a url.
        lower score = higher priority.
        """
        # parsed url
        parsed = urlparse(url)

        # get number of params after '?' in url
        num_params = len(parse_qsl(parsed.query))

        return num_params, len(url)

    return sorted(valid_urls, key=score)


def saved_domains_to_files():
    all_doms, blocked_doms, allowed_doms = filter_domains()

    save_to_text_file(
        "\n".join(sorted(all_doms)), DOMAINS_PATH, "all_domain.txt", logger
    )
    save_to_text_file(
        "\n".join(sorted(allowed_doms)), DOMAINS_PATH, "allowed_domain.txt", logger
    )
    save_to_text_file(
        "\n".join(sorted(blocked_doms)), DOMAINS_PATH, "blocked_domain.txt", logger
    )

    logger.info(f"SAVED DOMAINS TO {DOMAINS_PATH}")


def run_url_filter():
    products = get_product_list()
    filtered_products = []

    for product in products:
        product_id = product.get("product_id")
        urls = product.get("urls", [])

        # Filter url
        filtered_urls = scored_url(urls)

        if filtered_urls:
            filtered_products.append({"product_id": product_id, "urls": filtered_urls})

    os.makedirs(PRODUCT_URLS_FILTER_DIR, exist_ok=True)

    batch_size = PID_FILTER_BATCH_SIZE
    file_counter = 1
    total_saved = 0

    for idx in range(0, len(filtered_products), batch_size):
        batch = filtered_products[idx : idx + batch_size]
        filename = f"product_url_batch_{file_counter}.json"

        save_json_batch(
            data=batch,
            directory=PRODUCT_URLS_FILTER_DIR,
            filename=filename,
            logger=logger,
            message="FILTERED URLS | SAVED BATCH",
        )

        total_saved += len(batch)
        file_counter += 1

    logger.info(
        f"JOB END | FINISHED FILTERED URL. "
        f"Total {total_saved} allowed product across {file_counter - 1} files batch."
    )


if __name__ == "__main__":
    saved_domains_to_files()
    run_url_filter()
