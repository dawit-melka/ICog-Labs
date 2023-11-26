from fuzzywuzzy import fuzz

def check_similarity(sentence1, sentence2):
    similarity_ratio = fuzz.ratio(sentence1, sentence2)

    threshold = 80

    if similarity_ratio >= threshold:
        return True
    else:
        return False
