# Weed/Plant Segmentation Annotation App

## Overview
This project is designed to create a **high-quality segmentation-based annotated dataset** for weed and plant detection on fallow land. Unlike bounding boxes, annotations are **pixel-accurate masks**, which is crucial for training semantic or instance segmentation models in agriculture.

## Features
- Automatic dataset download from KaggleHub (`jaidalmotra/weed-detection`)
- Streamlit interface for selecting and viewing images
- Placeholder for segmentation annotation
- Ready to integrate with polygon/mask drawing tools

## Requirements
- Python 3.11.0
- Streamlit
- KaggleHub
- Pillow, OpenCV, Numpy

## Installation
```bash
git clone <repo_url>
cd weed_segmentation_app
pip install -r requirements.txt
streamlit run app.py
