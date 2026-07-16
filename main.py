from parsers.resume_parser import read_pdf, clean_text
from parsers.experience_parser import ExperienceParser
from scoring.experience_engine import ExperienceEngine
import os
resume_path = os.path.join("data", "sampleresume.pdf")

text = read_pdf(resume_path)
cleaned_text = clean_text(text)

parser = ExperienceParser()
experiences = parser.extract_experience(cleaned_text)

engine = ExperienceEngine()

total_exp = engine.calculate_total_experience(experiences)
gaps = engine.detect_gaps(experiences)
overlaps = engine.detect_overlaps(experiences)

required_roles = [
    "AI Developer",
    "Machine Learning Engineer",
    "Python Developer"
]

score = engine.calculate_relevance_score(
    experiences,
    required_roles
)

print("\n========== DAY 10 REPORT ==========")
print(f"Total Experience (Months): {total_exp}")
print(f"Gaps: {gaps}")
print(f"Overlaps: {overlaps}")
print(f"Relevance Score: {score}")

print("\nStructured Experience:")
for exp in experiences:
    print(exp.model_dump())

from parsers.education_parser import EducationParser
from parsers.education_relevance import calculate_education_score
from parsers.resume_parser import read_pdf, clean_text

resume = "data/sampleresume.pdf"

text = read_pdf(resume)
text = clean_text(text)

from parsers.education_parser import AcademicProfile

parser = EducationParser()

education = parser.extract_education(text)
certifications = parser.extract_certifications(text)

profile = AcademicProfile(
    education=education,
    certifications=certifications
)

print("\n========== ACADEMIC PROFILE ==========\n")
print(profile.model_dump_json(indent=4))

score = calculate_education_score(profile)

print("\nEducation Relevance Score:", score)
