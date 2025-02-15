# VizAi

#Slides- https://docs.google.com/presentation/d/1u80asFoXy3CAD9kbjpGT07EIE81hVsMWVG9PRRlS4aQ/edit?usp=sharing
# FOOD SAGE - Processed Food Ingredient Analyzer

## Overview

This project focuses on identifying and extracting the ingredients section from processed food packaging. The extracted ingredients are then categorized into three levels of potential harmfulness. By leveraging computer vision and optical character recognition (OCR) techniques, the system analyzes the ingredient lists and assesses their relative health impact.

## Goals

1. **Extract Ingredients Section**: Automatically detect and isolate the ingredients list from processed food labels using image processing and OCR.
2. **Categorize Ingredients**: Group extracted ingredients into one of three categories based on their potential health effects:
   - **High Risk**: Ingredients that are generally considered harmful or controversial.
   - **Moderate Risk**: Ingredients that may be of concern depending on quantity, processing, or context.
   - **Low Risk/Generally Safe**: Ingredients widely regarded as safe under normal consumption.

3. **Enable Further Analysis**: Lay the groundwork for future enhancements, such as linking ingredients to scientific studies, providing substitution suggestions, and integrating with external databases.

## Technologies Used

- **OpenCV**: For image preprocessing, filtering, and feature detection.
- **Tesseract OCR**: For extracting text from the processed image regions.
- **Python**: The primary programming language used for the pipeline.
- **Jupyter Notebooks** (Optional): For experimenting with different preprocessing and analysis techniques.
- **GitHub Issues & Discussions**: To track progress, report bugs, and share ideas.

## Project Structure

```plaintext
.
├── README.md               # Project overview and documentation
├── src/                    # Source code for processing images and extracting text
│   ├── preprocess.py       # Image preprocessing steps (filtering, cropping, etc.)
│   ├── ocr.py              # OCR logic for extracting text
│   ├── categorize.py       # Categorization logic based on extracted text
│   └── main.py             # Main entry point for the pipeline
├── data/                   # Sample images and reference data
│   ├── images/             # Sample processed food packaging images
│   └── labels.json         # Reference ingredient labels and categories
├── tests/                  # Test scripts to ensure reliability
├── docs/                   # Additional documentation and references
└── requirements.txt        # Required Python dependencies
