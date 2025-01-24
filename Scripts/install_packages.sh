#!/bin/bash

# Initialize Conda
eval "$(conda shell.bash hook)"

# Create virtual environment
conda create -n analysis_of_portuguese_news python=3.12 -y

#Activate virtual environment
conda activate analysis_of_portuguese_news

# Upgrade pip
pip install --upgrade pip

# Install the packages
pip install nbformat
pip install nbconvert
pip install numpy
pip install pandas
pip install beautifulsoup4
pip install openpyxl
pip install matplotlib
pip install seaborn
pip install nltk
pip install spacy
pip install wordcloud
pip install pillow
pip install leia-br
pip install openai
pip install tiktoken
pip install scipy
pip install chromadb
pip install statsmodels

# Download the spaCy Portuguese model
python -m spacy download pt_core_news_lg

# Run the Python script for NLTK stopwords
python download_nltk_tools.py
