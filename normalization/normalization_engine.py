import re


class NormalizationEngine:

    def normalize_text(self, text):

        text = text.lower()

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def mask_personal_information(self, text):

        patterns = [
            r"name\s*:\s*.*",
            r"gender\s*:\s*.*",
            r"age\s*:\s*.*",
            r"date of birth\s*:\s*.*",
            r"dob\s*:\s*.*",
            r"religion\s*:\s*.*",
            r"marital status\s*:\s*.*",
            r"nationality\s*:\s*.*",
            r"address\s*:\s*.*",
        ]

        for pattern in patterns:
            text = re.sub(pattern, "[MASKED]", text, flags=re.IGNORECASE)

        return text

    def normalize_score(self, score):

        if score < 0:
            return 0

        if score > 100:
            return 100

        return round(score, 2)

    def bias_risk(self, text):

        keywords = [
            "male",
            "female",
            "religion",
            "married",
            "single",
            "dob",
            "date of birth",
            "nationality"
        ]

        for word in keywords:
            if word in text.lower():
                return "Medium"

        return "Low"