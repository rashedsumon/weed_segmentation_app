import streamlit as st
from data_loader import download_weed_dataset
import os
from pathlib import Path
from PIL import Image
import numpy as np

st.set_page_config(page_title="Weed Segmentation Annotator", layout="wide")
st.title("Weed/Plant Segmentation Annotation Tool")

# -------------------------
# Download dataset
# -------------------------
dataset_path = download_weed_dataset()
st.write(f"Dataset downloaded to: {dataset_path}")

# Load all images
image_dir = Path(dataset_path) / "images"
image_files = list(image_dir.glob("*.jpg")) + list(image_dir.glob("*.png"))

if not image_files:
    st.warning("No images found in dataset.")
else:
    st.sidebar.header("Select Image to Annotate")
    selected_image = st.sidebar.selectbox("Image", image_files)

    img = Image.open(selected_image)
    st.image(img, caption=f"Annotating: {selected_image.name}", use_column_width=True)

    # -------------------------
    # Annotation placeholder
    # -------------------------
    st.markdown("### Draw masks (Segmentation)")
    st.info("This is a placeholder for segmentation tool integration. "
            "You can integrate a JS/Canvas-based annotation library "
            "or use Streamlit components for polygon/mask drawing.")

    # -------------------------
    # Save mask placeholder
    # -------------------------
    st.button("Save Mask")
    st.success("Mask saved (placeholder). Integration with real annotation tool required).")
