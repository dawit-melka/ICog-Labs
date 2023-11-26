from sentence_transformers import SentenceTransformer, util
import os
import nltk
import time
import matplotlib.pyplot as plt
import numpy as np

from data.questions_and_answers import questions, answers
from utils.check_sentence_similarity import check_similarity

# nltk.download('punkt')  # Uncomment if not already downloaded

def load_input_data(file_path):
    """
    Load input data from a file.

    Parameters:
    - file_path (str): Path to the input file.

    Returns:
    - str: Contents of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def convert_to_sentences(text):
    """
    Convert a text into a list of sentences.

    Parameters:
    - text (str): Input text.

    Returns:
    - list: List of sentences.
    """
    return nltk.sent_tokenize(text)

def download_models(model_names):
    """
    Download sentence transformer models.

    Parameters:
    - model_names (list): List of model names to download.
    """
    for model_name in model_names:
        model = SentenceTransformer(model_name)

def compute_similarity_scores(query_emb, doc_emb):
    """
    Compute similarity scores between a query and document embeddings.

    Parameters:
    - query_emb (numpy array): Embedding of the query.
    - doc_emb (numpy array): Embeddings of the documents.

    Returns:
    - list: Similarity scores.
    """
    return util.dot_score(query_emb, doc_emb)[0].cpu().tolist()

def main():
    # Define constants
    INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), '.\\data\\to_kill_a_mocking_bird.txt')
    MODELS = ['multi-qa-mpnet-base-dot-v1', 'all-mpnet-base-v2', 'multi-qa-distilbert-cos-v1',
              'all-distilroberta-v1', 'all-MiniLM-L12-v2', 'multi-qa-MiniLM-L6-cos-v1', 'msmarco-distilbert-dot-v5']

    # Load input data
    data = load_input_data(INPUT_FILE_PATH)

    # Convert the book into a list of sentences
    book_sentences = convert_to_sentences(data)

    # Download all models
    download_models(MODELS)

    model_stats = {}

    for model_name in MODELS:
        start_time = time.time()
        print(model_name, "model running...")

        # Load the model
        model = SentenceTransformer(model_name)

        # Encode query and documents
        doc_emb = model.encode(book_sentences, convert_to_tensor=True)
        error = 0
        count_first_result = 0
        count_second_result = 0
        count_third_result = 0
        count_top_10 = 0

        # Implementation of the semantic search logic...
        for i, query in enumerate(questions):
            query_emb = model.encode(query, convert_to_tensor=True)

            # Compute dot score between query and all document embeddings
            scores = compute_similarity_scores(query_emb, doc_emb)

            # Combine docs & scores
            doc_score_pairs = list(zip(book_sentences, scores))

            # Sort by decreasing score
            doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)

            # Output passages & scores
            top_k = 10
            found = False
            for j in range(1, top_k + 1):
                if check_similarity(doc_score_pairs[j][0], answers[i]):
                    error += (j - 1)
                    found = True
                    count_first_result += 1 if j == 1 else 0
                    count_second_result += 1 if j == 2 else 0
                    count_third_result += 1 if j == 3 else 0
                    count_top_10 += 1
                    break

            if not found:
                error += 15
            print(i + 1, "/", len(questions), " error: ", error, "count found: ", count_top_10)

        end_time = time.time()
        model_stats[model_name] = {"time elapsed": end_time - start_time,
                                   "total error": error,
                                   "total found": count_top_10,
                                   "first results": count_first_result,
                                   "second results": count_second_result,
                                   "third results": count_third_result}
        print(model_name, " model status \n", model_stats[model_name])
    print(model_stats)


if __name__ == "__main__":
    main()
