"""
Housekeeping DAG.

Cleans up old Airflow logs, project custom logs, and raw JSON/Parquet data
that are older than 30 days to free up disk space.

Schedule: Daily at midnight.
"""

from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

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

# ─── DAG Definition ──────────────────────────────────────────────────

with DAG(
    dag_id="housekeeping_pipeline",
    default_args=default_args,
    description="Clean up Airflow logs, project logs, and raw data > 30 days",
    schedule="0 0 * * *",  # Runs daily at midnight
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["maintenance", "cleanup", "batch"],
    doc_md=__doc__,
) as dag:
    # 1. Clean Airflow internal task logs
    # Deletes log files older than 30 days, then removes any empty directories left behind.
    clean_airflow_logs = BashOperator(
        task_id="clean_airflow_logs",
        bash_command="""
        echo "Cleaning Airflow logs older than 30 days..."
        find /opt/airflow/logs -type f -mtime +30 -delete || true
        find /opt/airflow/logs -type d -empty -delete || true
        echo "Done."
        """,
        doc_md="Delete Airflow task logs older than 30 days",
    )

    # 2. Clean custom project logs (from config/logger.py)
    # The custom logs are stored in /opt/airflow/project/logs
    clean_project_logs = BashOperator(
        task_id="clean_project_logs",
        bash_command="""
        echo "Cleaning Project custom logs older than 30 days..."
        find /opt/airflow/project/logs -type f -name '*.log*' -mtime +30 -delete || true
        find /opt/airflow/project/logs -type d -empty -delete || true
        echo "Done."
        """,
        doc_md="Delete custom project logs older than 30 days",
    )

    # 3. Clean raw JSON/Parquet data
    # The extraction saves files to /opt/airflow/project/data (e.g. product_info, ip2location)
    clean_raw_data = BashOperator(
        task_id="clean_raw_data",
        bash_command="""
        echo "Cleaning Raw JSON and Parquet data older than 30 days..."
        find /opt/airflow/project/data -type f -name '*.json' -mtime +30 -delete || true
        find /opt/airflow/project/data -type d -empty -delete || true
        echo "Done."
        """,
        doc_md="Delete raw JSON files in data folder older than 30 days",
    )

    # ── Dependencies ─────────────────────────────────────────────────
    clean_airflow_logs >> clean_project_logs >> clean_raw_data
