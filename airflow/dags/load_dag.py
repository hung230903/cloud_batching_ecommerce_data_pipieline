"""
Load DAG — Stage 2 of the batch data pipeline.

Orchestrates loading extracted data to Google Cloud Storage (GCS)
and then into BigQuery:

  1. Three parallel GCS uploads:
     - load_ip2location_to_gcs
     - load_product_info_to_gcs
     - load_summary_to_gcs
  2. Manual BigQuery load (fallback / verification)

Note: The Cloud Function (GCS → BigQuery event trigger) should be
deployed beforehand via the separate 'deploy_cloud_functions' DAG.
Once deployed, each GCS upload automatically triggers ingestion
into BigQuery via the object.finalize event.

Configuration uses environment variables forwarded from docker-compose.yaml,
which reads from the project's .env file.
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
    "retries": 2,
    "retry_delay": timedelta(minutes=3),
}

# ─── Task Callables ──────────────────────────────────────────────────


def _load_ip2location_to_gcs(**kwargs):
    """Convert IP2Location JSON files to Parquet and upload to GCS."""
    import os

    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)
    from loaders.gcs_loader.load_ip2location_to_gcs import run_load_ip2location

    run_load_ip2location()


def _load_product_info_to_gcs(**kwargs):
    """Convert product info JSON files to Parquet and upload to GCS."""
    import os

    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)
    from loaders.gcs_loader.load_product_info_to_gcs import run_load_product_to_gcs

    run_load_product_to_gcs()


def _load_summary_to_gcs(**kwargs):
    """Read summary BSON file, convert to Parquet, and upload to GCS."""
    import os

    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)
    from loaders.gcs_loader.load_summary_to_gcs import run_load_summary

    run_load_summary()


def _load_gcs_to_bigquery(**kwargs):
    """Manually load Parquet files from GCS into BigQuery."""
    from loaders.gcs_to_bq import run_load

    run_load()


# ─── DAG Definition ──────────────────────────────────────────────────

with DAG(
    dag_id="batch_load_pipeline",
    default_args=default_args,
    description="Stage 2: Load data to GCS and BigQuery",
    schedule="@once",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["batch", "load", "gcs", "bigquery"],
    doc_md=__doc__,
) as dag:
    # ── Step 1: Parallel GCS uploads ─────────────────────────────────
    # Each upload triggers the Cloud Function via object.finalize event
    # (Cloud Function must be deployed first via deploy_cloud_functions DAG)

    load_ip_gcs = PythonOperator(
        task_id="load_ip2location_to_gcs",
        python_callable=_load_ip2location_to_gcs,
        execution_timeout=timedelta(hours=2),
        doc_md="Upload ip2location Parquet files to GCS",
    )

    load_product_gcs = PythonOperator(
        task_id="load_product_info_to_gcs",
        python_callable=_load_product_info_to_gcs,
        execution_timeout=timedelta(hours=2),
        doc_md="Upload product info Parquet files to GCS",
    )

    load_summary_gcs = PythonOperator(
        task_id="load_summary_to_gcs",
        python_callable=_load_summary_to_gcs,
        execution_timeout=timedelta(hours=4),
        doc_md="Upload summary Parquet files to GCS (30G+ BSON source)",
    )

    # ── Step 2: Manual BigQuery Load (fallback / verification) ───────

    load_bq = PythonOperator(
        task_id="load_gcs_to_bigquery",
        python_callable=_load_gcs_to_bigquery,
        execution_timeout=timedelta(hours=2),
        doc_md="Fallback: verify and load any missing Parquet from GCS into BigQuery",
    )

    # ── Dependencies ─────────────────────────────────────────────────
    # Parallel GCS uploads → manual BQ load (fallback/verification)
    [load_ip_gcs, load_product_gcs, load_summary_gcs] >> load_bq
