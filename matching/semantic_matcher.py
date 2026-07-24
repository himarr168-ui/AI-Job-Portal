from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticMatcher:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def read_text_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    def calculate_similarity(self, resume_text, jd_text):

        if not resume_text or not jd_text:
            return 0.0

        vectors = self.vectorizer.fit_transform([
            resume_text,
            jd_text
        ])

        score = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        return round(float(score), 2)

    def get_match_label(self, score):

        if score >= 0.80:
            return "Excellent Match"

        elif score >= 0.60:
            return "Good Match"

        elif score >= 0.40:
            return "Average Match"

        else:
            return "Poor Match"
