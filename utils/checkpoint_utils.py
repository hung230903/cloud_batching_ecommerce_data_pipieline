import json
import os

from config.base import CHECKPOINT_DIR


def _get_checkpoint_path(job_name):
    # Create checkpoint file base on job name
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    return os.path.join(CHECKPOINT_DIR, f"{job_name}_checkpoint.json")


def get_checkpoint(job_name):
    """
    Read checkpoint from file
    If JSON return dictionary else string
    """
    path = _get_checkpoint_path(job_name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return None
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return content
    return None


def save_checkpoint(job_name, value):
    """
    Save new checkpoint value for a job to file.
    If value is a dict, save as a JSON string.
    """
    path = _get_checkpoint_path(job_name)
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(value, dict):
            f.write(json.dumps(value))
        else:
            f.write(str(value))


def get_checkpoint_manager(job_name):
    """
    Utility to quickly create a manager based on job name.
    """

    class SimpleManager:
        def get_checkpoint(self):
            return get_checkpoint(job_name)

        def save_checkpoint(self, value):
            return save_checkpoint(job_name, value)

    return SimpleManager()
