from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticMatcher:

    def read_text_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def calculate_similarity(self, resume_text, jd_text):

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform([
            resume_text,
            jd_text
        ])

        score = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        return float(score)

    def get_match_label(self, score):

        if score >= 0.80:
            return "Excellent Match"

        elif score >= 0.60:
            return "Good Match"

        elif score >= 0.40:
            return "Average Match"

        else:
            return "Poor Match"

