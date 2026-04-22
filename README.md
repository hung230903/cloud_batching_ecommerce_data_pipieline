# 💎 Glamira Data Engineering Project - E-commerce Analytics

An end-to-end data engineering pipeline built with **Python**, **dbt**, and **Google Cloud Platform (GCP)** to collect, process, and analyze data from the Glamira e-commerce platform. The project implements a modern data stack with a Medallion Architecture in BigQuery.

---

## 📋 Table of Contents

- [Data Pipeline Stages](#-data-pipeline-stages)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Data Modeling](#-data-modeling)
- [Configuration](#-configuration)
- [Getting Started](#-getting-started)
- [Monitoring](#-monitoring)

---

## 🚀 Data Pipeline Stages

The pipeline is organized into modular stages executed sequentially to transform raw web data into analytical insights.

| Stage                        | Description                                                                            |
| :--------------------------- | :------------------------------------------------------------------------------------- |
| **Stage 1: IP to Location**  | Converts raw user IP addresses into geographic data using IP2Location LITE DB.         |
| **Stage 2: PID Filter**      | Filters and identifies new Product IDs (PIDs) for crawling from summary logs.          |
| **Stage 3: Product Crawler** | Asynchronously crawls detailed product info (name, price, SKU, options) from Glamira.  |
| **Stage 4: Storage Sync**    | Synchronizes processed data to Google Cloud Storage (GCS) in Optimized Parquet format. |
| **Stage 5: BigQuery Load**   | Orchestrates the ingestion of Parquet files from GCS into BigQuery raw tables.         |

---

## 🛠 Tech Stack

| Category                   | Technology                          |
| :------------------------- | :---------------------------------- |
| **Language**               | Python 3.13+                        |
| **Data Orchestration**     | Custom Python Runner (`main.py`)    |
| **Database (Raw/Staging)** | MongoDB, Google Cloud Storage (GCS) |
| **Data Warehouse**         | Google BigQuery                     |
| **Transformation**         | dbt (data build tool)               |
| **Visualization**          | Streamlit, Plotly                   |
| **Cloud Provider**         | Google Cloud Platform (GCP)         |
| **Package Manager**        | uv                                  |

---

## 📁 Project Structure

```text
.
├── config/                 # Central configuration and logging management
│   ├── base.py             # Environment variables and global project constants
│   └── logger.py           # Standardized logger setup for all modules
├── extract/                # Data collection and filtering logic
│   ├── pid_filter.py       # Identifies unique Product IDs (PIDs) from interaction logs
│   └── product_crawler.py  # Asynchronous high-performance product info crawler
├── loaders/                # Data movement and storage synchronization
│   ├── gcs_to_bq.py        # Script to trigger BigQuery Load Jobs from GCS Parquet
│   ├── load_ip_to_mongo.py # Maps IPs to Geo-data and persists to MongoDB
│   ├── load_product_to_gcs.py # Syncs local crawled product info to GCS (JSON -> Parquet)
│   └── load_summary_to_gcs.py # Syncs raw logs from MongoDB to GCS (BSON -> Parquet)
├── monitoring/             # Health checks and data quality assurance
│   ├── data_profiler.py    # Generates deep profiling reports and data dictionaries
│   └── e2e_test.py         # End-to-end integration testing for the entire flow
├── processing/             # Transformation and enrichment utilities
│   ├── ip_transformer.py   # Core logic for IP2Location data transformation
│   ├── product_info_extractor.py # Parse and structure HTML data from Glamira
│   └── summary_transformer.py # Clean and map log event schemas to analytical models
├── transform/              # Primary transformation layer (dbt)
│   └── glamira_dbt/        # dbt project for Dimensional Modeling (SCD Type 2)
│       ├── models/         # Staging, Transform, and Mart (Star Schema) layers
│       └── snapshots/      # SCD Type 2 tracking for Customer dimension
├── utils/                  # Reusable helper functions
│   ├── checkpoint_utils.py # Manage job checkpoints for pipeline resumes
│   ├── file_saving_utils.py # Standardized handlers for JSON/binary file saving
│   └── time_utils.py       # Utilities for time formatting and measurement
├── dashboard/              # Streamlit-based executive analytics dashboard
├── main.py                 # Main entry point to orchestrate the ETL execution
├── pyproject.toml          # Project dependencies (uv, pandas, bigquery, etc.)
└── .env.example            # Configuration template for local environment setup
```

---

## ✨ Features

### 🕷 Intelligent Web Crawling

- High-performance asynchronous crawling using `aiohttp`.
- Semaphore-based rate limiting and automatic retry logic.
- Intelligent PID filtering to avoid redundant data collection.

### 🌍 Data Enrichment

- IP2Location integration for precise user location mapping.
- Product option flattening (colours, metals, stones) for granular analysis.

### 🏗 Modern Data Warehousing

- **Medallion Architecture**: Raw (Bronze) → Staging (Silver) → Mart (Gold).
- **Star Schema Design**: Optimized for analytical queries in BigQuery.
- **SCD Type 2 Tracking**: Historical versioning for customer attributes using dbt Snapshots.

---

## 📊 Data Modeling (dbt)

The transformation layer builds a robust Star Schema within BigQuery:

- **Fact Tables**: `fact_sales_order` (sales transactions and product interactions).
- **Dimension Tables**:
  - `dim_product`, `dim_customer` (SCD Type 2), `dim_location`.
  - `dim_colour`, `dim_metal`, `dim_stone`, `dim_store`.
  - `dim_date` (standardized time analysis).

---

## ⚙️ Configuration

The system uses a `.env` file for secure configuration. Copy the example and update your credentials:

```bash
cp .env.example .env
```

| Key               | Description                                |
| :---------------- | :----------------------------------------- |
| `MONGODB_URI`     | Connection string for the raw data source. |
| `GCS_BUCKET_NAME` | Destination bucket for Parquet files.      |
| `BQ_PROJECT_ID`   | Your Google Cloud Project ID.              |
| `BQ_DATASET_ID`   | Targeted BigQuery dataset name.            |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Google Cloud SDK (authenticated)
- `uv` package manager

### Installation

```bash
# Sync dependencies
uv sync
```

### Execution

```bash
# Run the full data pipeline (Extract & Load)
python main.py

# Run dbt snapshots (Capture historical changes for SCD Type 2)
cd transform/glamira_dbt
dbt snapshot

# Run transformations (Build Star Schema)
dbt run
```

### View Dashboard

```bash
streamlit run dashboard.py
```

---

## 📊 Monitoring

The pipeline tracks execution and data quality:

- **Logging**: Integrated Python logging with stage-specific markers.
- **dbt tests**: Schema and data validation tests run after transformations.
- **Data Profiling**: Internal profiling tools to generate data dictionaries.

---

## 📄 License

This project is for educational purposes.
