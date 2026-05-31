import logging
import subprocess

from extract.product.product_crawler import run_product_crawler
from loaders.main_gcs_export import export_all
from loaders.mongo_loader.load_enriched_ip_to_mongo import load_enriched_ip_to_mongo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def stage_1_extract():
    logger.info(" --- STAGE 1: EXTRACT DATA FOR PIPELINE ---")

    logger.info(" --- STEP 1: IP EXTRACTION ---")
    load_enriched_ip_to_mongo()

    logger.info(" --- STEP 2: PRODUCT INFO EXTRACTION ---")
    run_product_crawler()


def load_step():
    logger.info(" --- STAGE 2: LOAD DATA TO GCS ---")
    export_all()


def stage_2_load():
    logger.info("--- STAGE 2: LOAD ---")

    logger.info("- STEP 1: Export to GCS with Cloud Functions -")
    # Export all
    export_all()

    # Manual export (Commented out)
    # run_load_ip2location()
    # run_load_summary()
    # run_load_product_to_gcs()

    logger.info("- STEP 2: Deploy Cloud Functions to GCP -")
    # Uncomment and replace YOUR_GCS_BUCKET_NAME with your actual bucket name to deploy
    try:
        logger.info("Deploying gcs_to_bq cloud function...")
        subprocess.run(
            [
                "gcloud",
                "functions",
                "deploy",
                "gcs_to_bq",
                "--runtime",
                "python310",
                "--trigger-resource",
                "YOUR_GCS_BUCKET_NAME",
                "--trigger-event",
                "google.storage.object.finalize",
                "--entry-point",
                "trigger_bigquery_load",
                "--source",
                "cloud_functions/gcs_to_bq",
                "--region",
                "CHOOSE_YOUR_REGION",  # Change to your region if needed
            ],
            check=True,
        )
        logger.info("Cloud Function deployed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to deploy Cloud Function: {e}")
        raise

    logger.info("- STEP 3: Export to BigQuery manually -")
    # bq_load()


def stage_3_transform():
    logger.info("--- STAGE 3: TRANSFORM ---")
    logger.info("- STEP 1: Run dbt models -")
    try:
        # Run dbt inside the transform/glamira_dbt directory
        subprocess.run(["dbt", "run"], cwd="transform/glamira_dbt", check=True)
        logger.info("dbt run completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"dbt run failed with error: {e}")
        raise


def main():
    logger.info("=== STARTING FULL DATA PIPELINE FLOW ===")

    try:
        stage_1_extract()
        stage_2_load()
        stage_3_transform()

        logger.info("=== DATA PIPELINE COMPLETED SUCCESSFULLY ===")
    except Exception as e:
        logger.error(f"PIPELINE FAILED: {e}")


if __name__ == "__main__":
    main()
