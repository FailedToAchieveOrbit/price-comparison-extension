# nlp_utils.py
import spacy

class NLPUtils:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg')

    def preprocess_title(self, title):
        doc = self.nlp(title)
        tokens = [token for token in doc if not (token.is_stop or token.is_punct)]
        return tokens

    def compare_titles(self, title1, title2, similarity_threshold=0.8):
        preprocessed_title1 = self.preprocess_title(title1)
        preprocessed_title2 = self.preprocess_title(title2)
        similarity_score = self.compute_similarity(preprocessed_title1, preprocessed_title2)
        return similarity_score >= similarity_threshold

    def compute_similarity(self, tokens1, tokens2):
        token_vectors1 = [token.vector for token in tokens1 if token.has_vector]
        token_vectors2 = [token.vector for token in tokens2 if token.has_vector]

        if not token_vectors1 or not token_vectors2:
            return 0.0

        avg_vector1 = sum(token_vectors1) / len(token_vectors1)
        avg_vector2 = sum(token_vectors2) / len(token_vectors2)

        return self.nlp(avg_vector1).similarity(self.nlp(avg_vector2))
