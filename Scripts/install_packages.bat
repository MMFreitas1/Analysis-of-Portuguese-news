@echo off

REM Initialize Conda
CALL conda init

REM Create virtual environment
CALL conda create -n analysis_of_portuguese_news python=3.12 -y

REM Activate virtual environment
CALL conda activate analysis_of_portuguese_news

REM Upgrade pip
CALL python -m pip install --upgrade pip

REM Install the packages
CALL pip install nbformat
CALL pip install nbconvert
CALL pip install numpy
CALL pip install pandas
CALL pip install beautifulsoup4
CALL pip install openpyxl
CALL pip install matplotlib
CALL pip install seaborn
CALL pip install nltk
CALL pip install spacy
CALL pip install wordcloud
CALL pip install pillow
CALL pip install leia-br
CALL pip install openai
CALL pip install tiktoken
CALL pip install scipy
CALL pip install chromadb
CALL pip install statsmodels


REM Download spaCy's Portuguese model
CALL python -m spacy download pt_core_news_lg

REM Run the Python script for NLTK stopwords
CALL python download_nltk_tools.py

echo Script execution finished!
pause
