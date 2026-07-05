"""
Transform DAG — Stage 3 of the batch data pipeline.

Runs dbt transformations on BigQuery data:
  raw_layer → staging → intermediate → data mart

Uses BashOperator to execute dbt commands inside the container.
Flow:
  dbt_deps → dbt_seed → dbt_run → dbt_test
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
    "retry_delay": timedelta(minutes=3),
}

# ─── Constants ────────────────────────────────────────────────────────

DBT_PROJECT_DIR = "/opt/airflow/project/transform/glamira_dbt"
DBT_PROFILES_DIR = "/opt/airflow/project/transform/glamira_dbt"
DBT_EXEC = "/home/airflow/dbt_venv/bin/dbt"

# ─── DAG Definition ──────────────────────────────────────────────────

with DAG(
    dag_id="batch_transform_pipeline",
    default_args=default_args,
    description="Stage 3: Run dbt transformations (staging → intermediate → mart)",
    schedule="@once",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["batch", "transform", "dbt", "bigquery"],
    doc_md=__doc__,
) as dag:
    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {DBT_PROJECT_DIR} && {DBT_EXEC} deps --profiles-dir {DBT_PROFILES_DIR}",
        doc_md="Install dbt package dependencies",
    )

    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command=f"cd {DBT_PROJECT_DIR} && {DBT_EXEC} seed --profiles-dir {DBT_PROFILES_DIR}",
        doc_md="Load seed files (e.g. translation mappings) into BigQuery",
    )

    dbt_run_staging = BashOperator(
        task_id="dbt_run_staging",
        bash_command=f"cd {DBT_PROJECT_DIR} && {DBT_EXEC} run --select staging --profiles-dir {DBT_PROFILES_DIR}",
        execution_timeout=timedelta(hours=2),
        doc_md="Run dbt staging models (raw → staging)",
    )

    dbt_run_intermediate = BashOperator(
        task_id="dbt_run_intermediate",
        bash_command=f"cd {DBT_PROJECT_DIR} && {DBT_EXEC} run --select intermediate --profiles-dir {DBT_PROFILES_DIR}",
        execution_timeout=timedelta(hours=2),
        doc_md="Run dbt intermediate models (staging → intermediate)",
    )

    dbt_run_mart = BashOperator(
        task_id="dbt_run_mart",
        bash_command=f"cd {DBT_PROJECT_DIR} && {DBT_EXEC} run --select mart --profiles-dir {DBT_PROFILES_DIR}",
        execution_timeout=timedelta(hours=2),
        doc_md="Run dbt mart models (intermediate → data mart)",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_PROJECT_DIR} && {DBT_EXEC} test --profiles-dir {DBT_PROFILES_DIR}",
        execution_timeout=timedelta(hours=1),
        doc_md="Run dbt tests to validate data quality",
    )

    # ── Dependencies ─────────────────────────────────────────────────
    (
        dbt_deps
        >> dbt_seed
        >> dbt_run_staging
        >> dbt_run_intermediate
        >> dbt_run_mart
        >> dbt_test
    )
