
# Project Documentation: AI Web Scraper

## Overview
This project is a web scraping application built using Python and Streamlit, designed to extract and display data from websites in an interactive interface.

## Prerequisites
- Python 3.8+
- Basic understanding of virtual environments and Python package management
- Streamlit for creating the web interface

## Setup Guide

### 1. Create a Python Virtual Environment
To ensure a clean environment for the project dependencies, it's recommended to create a virtual environment. Follow these steps:

\`\`\`bash
# Create a virtual environment
python -m venv ai-webscrapper

# Activate the virtual environment
# On Windows:
ai-webscrapper\Scripts\activate

# On MacOS/Linux:
source ai-webscrapper/bin/activate
\`\`\`

### 2. Install Dependencies
Once the virtual environment is activated, install the project dependencies listed in the \`requirements.txt\` file:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

This will install all the required packages, including Streamlit and any other necessary libraries.

### 3. Running the Application
To launch the web scraper, run the following command within the activated virtual environment:

\`\`\`bash
streamlit run main.py
\`\`\`

This will start a local web server, and you can access the application in your browser at \`http://localhost:8501\`.

## Usage
Once the application is running, you can use the provided interface to input target websites and scrape data.