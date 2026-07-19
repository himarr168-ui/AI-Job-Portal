import os

from parsers.resume_parser import read_pdf, clean_text
from matching.semantic_matcher import SemanticMatcher


class CandidateRanker:

    def __init__(self):
        self.matcher = SemanticMatcher()

    def get_status(self, score):

        if score >= 80:
            return "Shortlisted"

        elif score >= 60:
            return "Review"

        else:
            return "Rejected"

    def rank_candidates(self, resume_folder, jd_file):

        candidates = []

        jd_text = self.matcher.read_text_file(jd_file)

        for file in os.listdir(resume_folder):

            if file.endswith(".pdf"):

                resume_path = os.path.join(resume_folder, file)

                resume_text = clean_text(
                    read_pdf(resume_path)
                )

                similarity = self.matcher.calculate_similarity(
                    resume_text,
                    jd_text
                )

                ats_score = round(similarity * 100, 2)

                candidates.append(
                    {
                        "candidate": file,
                        "ats_score": ats_score,
                        "status": self.get_status(ats_score)
                    }
                )

        candidates.sort(
            key=lambda x: x["ats_score"],
            reverse=True
        )

        return candidates
