"""
Extract DAG — Stage 1 of the batch data pipeline.

Orchestrates two parallel extraction branches:
  Branch 1 (IP):      extract_unique_ips → enrich_ips → load_enriched_ip_to_mongo
  Branch 2 (Product):  pid_filter → url_filter → product_crawler

All task callables import from the existing project modules mounted
at /opt/airflow/project via PYTHONPATH.

This DAG is triggered manually (@once) since the extraction process
is a one-time batch operation on historical data.
"""

from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

from airflow import DAG

# ─── Default Arguments ────────────────────────────────────────────────

default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# ─── Task Callables ──────────────────────────────────────────────────


def _extract_unique_ips(**kwargs):
    """Extract unique IPs from MongoDB summary collection to a text file."""
    from extract.ip.ip_unique_filter import run_ip_unique_filter

    run_ip_unique_filter()


def _enrich_ips(**kwargs):
    """Enrich extracted IPs with geolocation data using IP2Location DB."""
    from extract.ip.get_enriched_ip import run_ip_enrichment

    run_ip_enrichment()


def _load_enriched_ip_to_mongo(**kwargs):
    """Load enriched IP data back into MongoDB."""
    from loaders.mongo_loader.load_enriched_ip_to_mongo import load_enriched_ip_to_mongo

    load_enriched_ip_to_mongo()


def _pid_filter(**kwargs):
    """Extract unique product IDs and URLs from MongoDB event collections."""
    from extract.product.pid_url_unique import run_pid_filter

    run_pid_filter()


def _url_filter(**kwargs):
    """Pre-process and filter product URLs (domain normalization, dedup)."""
    from processing.filter.product_urls_filter import run_url_filter

    run_url_filter()


def _product_crawler(**kwargs):
    """Crawl product pages to extract structured product data (react_data)."""
    from extract.product.product_crawler import run_product_crawler

    run_product_crawler()


# ─── DAG Definition ──────────────────────────────────────────────────

with DAG(
    dag_id="batch_extract_pipeline",
    default_args=default_args,
    description="Stage 1: Extract IP enrichment and product info from raw data",
    schedule="@once",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["batch", "extract"],
    doc_md=__doc__,
) as dag:
    # ── Branch 1: IP Enrichment ──────────────────────────────────────

    extract_unique_ips = PythonOperator(
        task_id="extract_unique_ips",
        python_callable=_extract_unique_ips,
        doc_md="Extract unique IPs from MongoDB → `data/ip2location/_unique_ips.txt`",
    )

    enrich_ips = PythonOperator(
        task_id="enrich_ips",
        python_callable=_enrich_ips,
        execution_timeout=timedelta(hours=6),
        doc_md="Enrich IPs with IP2Location DB → `data/ip2location/ip_enriched_batch_*.json`",
    )

    load_ip_to_mongo = PythonOperator(
        task_id="load_enriched_ip_to_mongo",
        python_callable=_load_enriched_ip_to_mongo,
        execution_timeout=timedelta(hours=2),
        doc_md="Upsert enriched IP records into MongoDB `ip2location` collection",
    )

    # # ── Branch 2: Product Crawling ───────────────────────────────────

    pid_filter = PythonOperator(
        task_id="pid_filter",
        python_callable=_pid_filter,
        execution_timeout=timedelta(hours=3),
        doc_md="Extract unique (product_id, urls) pairs from MongoDB → `data/pid_filter/`",
    )

    url_filter = PythonOperator(
        task_id="url_filter",
        python_callable=_url_filter,
        execution_timeout=timedelta(hours=1),
        doc_md="Normalize and filter product URLs → `data/product_urls_filter/`",
    )

    product_crawler = PythonOperator(
        task_id="product_crawler",
        python_callable=_product_crawler,
        execution_timeout=timedelta(hours=12),
        doc_md="Crawl product pages for react_data → `data/product_info/success/`",
    )

    # ── Dependencies ─────────────────────────────────────────────────
    # Two independent branches run in parallel

    # Branch 1: IP pipeline
    extract_unique_ips >> enrich_ips >> load_ip_to_mongo

    # Branch 2: Product pipeline
    pid_filter >> url_filter >> product_crawler
