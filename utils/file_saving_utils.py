import json
import os


def clean_json_data(obj):
    """
    Remove special keywords/characters in data fields
    """
    if isinstance(obj, str):
        return obj.replace("\r", "").strip()
    elif isinstance(obj, list):
        return [clean_json_data(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: clean_json_data(value) for key, value in obj.items()}
    return obj


def save_json_batch(
    data, directory, filename, logger, message="SAVED BATCH", clean_data=False
):
    """
    Generic function to save a list of data to a JSON file.
    """
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    if clean_data:
        data_to_save = clean_json_data(data)
    else:
        data_to_save = data

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    logger.info(f"{message} | TOTAL: {len(data_to_save)} | FILE: {filename}")


def save_to_text_file(data, directory, filename, logger, mode="w"):
    """
    Generic function to save data to text file.
    """
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    with open(filepath, mode, encoding="utf-8") as f:
        f.write(data + "\n")
    
    if mode == "w":
        logger.info(f"SAVED | TOTAL: {len(data)} | FILE: {filename}")
