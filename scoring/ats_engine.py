class ATSEngine:

    def __init__(self):

        # Default weight configuration
        self.weights = {
            "skills": 0.40,
            "experience": 0.30,
            "education": 0.10,
            "semantic": 0.20
        }

    def calculate_score(
        self,
        skill_score,
        experience_score,
        education_score,
        semantic_score
    ):

        final_score = (
            skill_score * self.weights["skills"] +
            experience_score * self.weights["experience"] +
            education_score * self.weights["education"] +
            semantic_score * self.weights["semantic"]
        )

        return round(final_score, 2)

    def recommendation(self, score):

        if score >= 80:
            return "Strongly Recommended"

        elif score >= 65:
            return "Recommended"

        elif score >= 50:
            return "Consider"

        else:
            return "Not Recommended"

    def generate_report(
        self,
        skill_score,
        experience_score,
        education_score,
        semantic_score
    ):

        final_score = self.calculate_score(
            skill_score,
            experience_score,
            education_score,
            semantic_score
        )

        report = {

            "Skill Score": skill_score,

            "Experience Score": experience_score,

            "Education Score": education_score,

            "Semantic Score": semantic_score,

            "Final ATS Score": final_score,

            "Recommendation": self.recommendation(final_score)

        }

        return report
