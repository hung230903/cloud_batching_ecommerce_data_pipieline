import pandas as pd

def transform_ip2location_data(df):
    """
    Biến đổi dữ liệu IP2Location để khớp với kiểu FLOAT trên BigQuery.
    """
    if 'latitude' in df.columns:
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    if 'longitude' in df.columns:
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    return df
