import pandas as pd
import json

def is_null(val):
    if val is None or val == "":
        return True
    if isinstance(val, (list, dict)):
        return False
    return pd.isna(val)

def safe_bool(val):
    if isinstance(val, list):
        if len(val) == 1:
            val = val[0]
        else:
            return None
            
    if is_null(val):
        return None
        
    s = str(val).lower().strip()
    if s in ['true', '1', 't', 'y', 'yes']:
        return True
    if s in ['false', '0', 'f', 'n', 'no']:
        return False
    return None

def safe_int(val):
    if isinstance(val, list):
        if len(val) == 1:
            val = val[0]
        else:
            return None
            
    if is_null(val):
        return None
        
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return None

def safe_float(val):
    if isinstance(val, list):
        if len(val) == 1:
            val = val[0]
        else:
            return None
            
    if is_null(val):
        return None
        
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def safe_string(val):
    if isinstance(val, list) and len(val) == 1:
        val = val[0]
        
    if is_null(val):
        return None
        
    if isinstance(val, (dict, list)):
        return json.dumps(val, ensure_ascii=False)
        
    return str(val)
