# Text Embedding Models Performance Analysis Project

## Overview

I undertook a project to analyze the performance of various text embedding models for a chatbot application. The goal was to evaluate different models in terms of their ability to represent text data effectively and to recommend suitable models for our specific use case.

## Tasks Completed

### 1. Data Collection

- **Web Scraping:** I collected data from web pages using a web scraper, converting each webpage into a separate .txt file.

- **PDF Extraction:** PDF documents were converted into text files (.txt) to make them suitable for embedding.

### 2. Data Preprocessing

I performed cleaning and preprocessing on the collected text data to ensure it was suitable for embedding. The following steps were taken:

- **HTML Cleaning:** HTML tags were removed using BeautifulSoup to clean web page text.

- **Text Cleaning:** Special characters were removed, and extra whitespaces were eliminated from the text.


### 3. Model Exploration

I researched and selected different text embedding models for experimentation. The [Hugging Face Model Hub](https://huggingface.co/spaces/mteb/leaderboard) served as a valuable resource for exploring and selecting models.

### 4. Embedding Experimentation [> Implementation](https://github.com/dawit-melka/ICog-Labs/blob/main/Chat%20Bot/Embedding%20Models%20Analysis/semantic_search.ipynb)

I evaluated the chosen embedding models on the preprocessed data. The process involved:

- Loading each model.
- Encoding the text data into vector representations.
- Analyzing the quality of the resulting vectors.
- Comparing the performance of different models.

### 5. Reporting and Documentation

I thoroughly documented the project, including:

- Details of chosen models, their architectures, and configurations.
- Experimental setup, including preprocessing steps and embedding procedures.
- Results of the performance analysis, highlighting the strengths and weaknesses of each model.

## Results

The project resulted in valuable insights into the performance of various text embedding models. The documentation provides a clear understanding of the chosen models, the experimental setup, and recommendations for further exploration or model selection.

  | Model                               | Time Elapsed (s) | Total Error | Total Found (21) | First Results | Second Results | Third Results | Dimension     | Size (MB)     |
  |-------------------------------------|------------------|-------------|------------------|---------------|----------------|---------------|---------------|---------------|
  | multi-qa-mpnet-base-dot-v1          | 87.77            | 117         | 16               | 6             | 2              | 2             | 768           | 420           |
  | msmarco-bert-base-dot-v5            | 96.15            | 135         | 14               | 4             | 3              | 3             | 768           | 420           |
  | hkunlp/instructor-xl                | 1595.49          | 158         | 14               | 2             | 0              | 3             | 768           | 4960          |
  | voyage-lite-01-instruct             | 355.76           | 166         | 12               | 2             | 5              | 0             | 1024          | -             |
  | thenlper/gte-large                  | 340.72           | 168         | 12               | 4             | 2              | 1             | 1024          | 670           |
  | multi-qa-distilbert-cos-v1          | 46.22            | 172         | 12               | 3             | 2              | 1             | 768           | 250           |
  | msmarco-distilbert-dot-v5           | 45.93            | 178         | 11               | 2             | 2              | 3             | 768           | 250           |
  | multi-qa-MiniLM-L6-cos-v1           | 14.61            | 183         | 11               | 4             | 0              | 0             | 384           | 80            |
  | hkunlp/instructor-large             | 395.49           | 188         | 11               | 1             | 2              | 2             | 768           | 1340          |
  | gtr-t5-xl                           | 1312.33          | 188         | 10               | 3             | 2              | 0             | 768           | 2370          | 
  | all-mpnet-base-v2                   | 89.32            | 191         | 10               | 4             | 1              | 1             | 768           | 420           | 
  | all-MiniLM-L12-v2                   | 27.07            | 203         | 10               | 2             | 1              | 0             | 384           | 120           | 
  | cohere-embed-english-v3.0           | 10.09            | 194         | 9                | 3             | 2              | 2             | 1024          | -             | 
  | all-distilroberta-v1                | 70.17            | 206         | 9                | 0             | 4              | 2             | 768           | 290           | 
  | sentence-t5-xl                      | 1517.48          | 209         | 9                | 2             | 2              | 1             | 768           | 2370          |
  | jamesgpt1/sf_model_e5               | 341.54           | 211         | 9                | 3             | 0              | 1             | 1024          | 1340          |
  | UAE-Large-v1                        | 2043.65          | 214         | 8                | 3             | 1              | 2             | 1024          | 1340          |
  | llmrails/ember-v1                   | 354.12           | 216         | 8                | 1             | 3              | 0             | 1024          | 1340          |
  | all-roberta-large-v1                | 485.51           | 234         | 7                | 1             | 1              | 1             | 1024          | 1360          |
  | BAAI/bge-large-en-v1.5              | 353.52           | 235         | 7                | 1             | 1              | 1             | 1024          | 1340          |
  | infgrad/stella-base-en-v2           | 96.30            | 241         | 7                | 1             | 0              | 2             | 768           | 220           |
  | jinaai/jina-embeddings-v2-base-en   | 132.16           | 246         | 6                | 1             | 1              | 0             | 768           | 270           |
  | intfloat/e5-large-v2                | 342.50           | 256         | 5                | 1             | 0              | 1             | 1024          | 1340          |




