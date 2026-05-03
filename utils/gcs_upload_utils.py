import io
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import storage
from config.logger import setup_logger

logger = setup_logger(
    name="gcs_upload",
    log_folder="loaders",
    log_file="gcs_upload.log",
)

def upload_buffer_to_gcs(buffer, bucket_name, destination_blob_name):
    """Upload a memory buffer to GCS."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_file(buffer, content_type="application/octet-stream")
        logger.info(f"SUCCESS Upload: gs://{bucket_name}/{destination_blob_name}")
        return True
    except Exception as e:
        logger.error(f"FAILED Upload {destination_blob_name}: {e}")
        return False

def _ensure_schema_columns(df, schema):
    """Đảm bảo DataFrame có đủ các cột theo schema, thêm cột thiếu nếu cần."""
    for name in schema.names:
        if name not in df.columns:
            if isinstance(schema.field(name).type, pa.ListType):
                df[name] = [[] for _ in range(len(df))]
            else:
                df[name] = None
    return df[schema.names]

def _write_batch_to_gcs(batch, collection_name, gcs_folder, part_idx, transform_func, schema, bucket_name):
    """Chuyển đổi một batch documents sang Parquet buffer và upload lên GCS."""
    logger.info(
        f"[{collection_name}] Writing part {part_idx} | "
        f"Batch size: {len(batch):,} records..."
    )

    df = pd.DataFrame(batch)
    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    if transform_func:
        df = transform_func(df)

    if schema:
        df = _ensure_schema_columns(df, schema)
        table = pa.Table.from_pandas(df, schema=schema)
    else:
        table = pa.Table.from_pandas(df)

    parquet_buffer = io.BytesIO()
    pq.write_table(table, parquet_buffer)
    parquet_buffer.seek(0)

    # Nếu part_idx là string (trong trường hợp file json), giữ nguyên tên, nếu là số thì format
    if isinstance(part_idx, str):
        destination = f"{gcs_folder}/{part_idx}"
    else:
        destination = f"{gcs_folder}/{collection_name}_part_{part_idx:04d}.parquet"
        
    upload_buffer_to_gcs(parquet_buffer, bucket_name, destination)
