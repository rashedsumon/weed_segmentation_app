import kagglehub
from pathlib import Path
import os
import zipfile

def download_weed_dataset():
    """
    Automatically download the latest weed detection dataset from KaggleHub.
    Returns the path to the extracted dataset folder.
    Handles both ZIP files and already-extracted directories.
    """
    dataset_name = "jaidalmotra/weed-detection"
    dataset_path = Path("datasets") / "weed_detection"

    if not dataset_path.exists():
        dataset_path.mkdir(parents=True, exist_ok=True)
        zip_path = kagglehub.dataset_download(dataset_name)

        # Check if the downloaded path is a file (ZIP) or directory
        zip_path = Path(zip_path)
        if zip_path.is_file() and zip_path.suffix in ['.zip']:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(dataset_path)
        elif zip_path.is_dir():
            # If already a directory, copy contents
            for item in zip_path.iterdir():
                target = dataset_path / item.name
                if item.is_dir():
                    os.system(f'cp -r "{item}" "{target}"')
                else:
                    os.system(f'cp "{item}" "{target}"')
        else:
            raise ValueError(f"Unexpected dataset format: {zip_path}")

    return str(dataset_path)
