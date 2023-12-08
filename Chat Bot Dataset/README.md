# Chatbot Dataset Project

## Introduction
This project involves the collection and preparation of a dataset for training a chatbot. The dataset is obtained from the website [https://investethiopia.gov.et/](https://investethiopia.gov.et/), and the goal is to create a clean and accurate dataset suitable for chatbot development.

## Steps Taken

### Step 1: Web Crawling
- Used a web crawler to navigate through the website and collect relevant data.
- The crawler saved each page's content in a separate text file.
- Extracted hyperlinks from each page to ensure comprehensive coverage of the website.
- Filtered hyperlinks to include only those within the same domain ([investethiopia.gov.et](https://investethiopia.gov.et/)).

### Step 2: PDF Handling
- Downloaded PDF files linked on the website.
- Renamed PDF files using their actual names instead of file paths.
- Converted the pdfs to text format utilizing OCR

### Step 3: Text Cleaning
- Removed unnecessary newlines, excess spaces, and irrelevant content.
- Implemented a function to remove gibberish and nonsensical words.
- Developed a function to keep only alphanumeric characters and dots, removing other symbols.
- Created a separate text file for each page.

### Step 4: Spell Checking and Correction
- Utilized a spell checker to correct spelling errors in the text files.

### Step 5: Manual Checking and Cleaning

- In addition to the automated processes, manual checking and cleaning were performed on the dataset. This involved a thorough review of each text file to address any specific issues that may not have been captured by automated methods.

### Step 6: Readme Generation
- Drafted this README file to document the steps taken in the project.

## Directory Structure

- raw_data/ # Contains the raw text files obtained from the web crawler.
- clean_data/ # Contains the cleaned and processed text files.
- web-crawl.py # Python script for web crawling and data processing. [OpenAI documentation](https://platform.openai.com/docs/tutorials/web-qa-embeddings).

