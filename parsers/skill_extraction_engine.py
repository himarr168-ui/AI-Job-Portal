import re

# Read cleaned resume
def read_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Master Skill Dictionary
MASTER_SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "TypeScript",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Vue",
    "Node.js",
    "Express",
    "Django",
    "Flask",
    "FastAPI",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "GCP",
    "REST API",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "TensorFlow",
    "PyTorch",
    "OpenCV",
    "AI",
    "Data Analysis",
    "Power BI",
    "Excel",
    "Communication",
    "Leadership",
    "Problem Solving"
]


# Skill Synonyms
SKILL_SYNONYMS = {
    "AI": "Artificial Intelligence",
    "ML": "Machine Learning",
    "JS": "JavaScript"
}


# Extract Skills
def extract_skills(text):
    found_skills = []

    # Replace synonyms
    for short, full in SKILL_SYNONYMS.items():
        text = re.sub(r"\b" + short + r"\b", full, text, flags=re.IGNORECASE)

    # Search skills
    for skill in MASTER_SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE):
            found_skills.append(skill)

    # Remove duplicates
    found_skills = list(dict.fromkeys(found_skills))

    return found_skills


# Confidence Score
def confidence_score(skills):
    scores = {}

    for skill in skills:
        scores[skill] = 95

    return scores


# Main
if __name__ == "__main__":

    resume_path = "data/clean_resume.txt"

    resume_text = read_resume(resume_path)

    skills = extract_skills(resume_text)

    scores = confidence_score(skills)

    output = {
        "skills": skills,
        "confidence": scores
    }

    print(output)

