# VizAi

# FOOD SAGE - Processed Food Ingredient Analyzer

<p align="center">
  <img src="Docs/powerpoint/pp_title.png" width="500" alt="UI layout for the FoodSage App." />
</p>

[Slides](https://docs.google.com/presentation/d/1u80asFoXy3CAD9kbjpGT07EIE81hVsMWVG9PRRlS4aQ/edit?usp=sharing)

<p align="center">
  <img src="Docs/app_mockup/ui_Collection.png" width="500" alt="UI layout for the FoodSage App." />
</p>

[Hi-Res](https://www.figma.com/design/pklM3epxNVo4HSGisRJAL9/Untitled?node-id=0-1&p=f&t=FlBFSLUj88XjPNYQ-0)

## Overview

This project focuses on identifying and extracting the ingredients section from processed food packaging. The extracted ingredients are then categorized into three levels of potential harmfulness. By leveraging computer vision and optical character recognition (OCR) techniques, the system analyzes the ingredient lists and assesses their relative health impact.

## Goals

1. **Extract Ingredients Section**: Automatically detect and isolate the ingredients list from processed food labels using image processing and OCR.

<p align="center">
  <img src="footage/OCRLabelTest.gif" width="500" alt="OCR Label Test">
</p>

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
```

## The Team

<p align="center">
  <img src="Docs/team_images/image_3.JPG" width="300" alt="FoodSage team busy at work." />
</p>
<p align="center">
  <img src="Docs/team_images/image_4.JPG" width="700" alt="FoodSage team creating the initial idea." />
</p>