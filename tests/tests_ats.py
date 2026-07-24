import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsers.resume_parser import read_pdf, clean_text
from matching.semantic_matcher import SemanticMatcher
from scoring.ats_engine import ATSEngine

# Resume folder
resume_folder = "data/resumes"

# Job Description
jd_path = "data/sample_jd.txt"

matcher = SemanticMatcher()
ats = ATSEngine()

jd_text = matcher.read_text_file(jd_path)

print("\n========== ATS SYSTEM TESTING ==========\n")

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        resume_path = os.path.join(resume_folder, file)

        resume_text = clean_text(read_pdf(resume_path))

        semantic_score = matcher.calculate_similarity(
            resume_text,
            jd_text
        ) * 100

        report = ats.generate_report(
            skill_score=75,
            experience_score=33,
            education_score=30,
            semantic_score=semantic_score
        )

        print(f"\nCandidate : {file}")
        print(report)
        print(f"ATS Score : {report['Final ATS Score']}")
        print(f"Recommendation : {report['Recommendation']}")
