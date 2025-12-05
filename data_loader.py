import kagglehub
from pathlib import Path
import os
import zipfile

def download_weed_dataset():
    """
    Automatically download the latest weed detection dataset from KaggleHub.
    Returns the path to the extracted dataset folder.
    """
    dataset_name = "jaidalmotra/weed-detection"
    dataset_path = Path("datasets") / "weed_detection"

    if not dataset_path.exists():
        dataset_path.mkdir(parents=True, exist_ok=True)
        zip_path = kagglehub.dataset_download(dataset_name)
        
        # Extract zip
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dataset_path)
    
    return str(dataset_path)
