FROM apache/airflow:2.10.4-python3.11

USER airflow

COPY requirements.txt .

# 1. Install regular dependencies with Airflow constraints to prevent conflicts
RUN pip install --no-cache-dir -r requirements.txt -c "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.11.txt"

# 2. Install dbt-bigquery in an isolated virtual environment to avoid pip backtracking hell
RUN python -m venv /home/airflow/dbt_venv && \
    /home/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-bigquery>=1.9.2

# 3. Add the isolated dbt executable to PATH
ENV PATH="/home/airflow/dbt_venv/bin:$PATH"

RUN rm requirements.txt
