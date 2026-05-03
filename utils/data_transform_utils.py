import pandas as pd
import json

def safe_bool(val):
    if pd.isna(val) or val == "" or val is None:
        return None
    s = str(val).lower().strip()
    if s in ['true', '1', 't', 'y', 'yes']:
        return True
    if s in ['false', '0', 'f', 'n', 'no']:
        return False
    return None

def safe_int(val):
    if val is None or pd.isna(val) or val == "":
        return None
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return None

def safe_float(val):
    if val is None or pd.isna(val) or val == "":
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def safe_string(val):
    if val is None or pd.isna(val):
        return None
    if isinstance(val, (dict, list)):
        return json.dumps(val, ensure_ascii=False)
    return str(val)
