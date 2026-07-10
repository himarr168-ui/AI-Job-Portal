def read_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
def classify_sections(text):
    sections = {
        "skills": [],
        "work_experience": [],
        "education": [],
        "certifications": [],
        "projects": []
    }

    current_section = None

    for line in text.split("\n"):
        line = line.strip()

        if line.lower() in ["skills", "technical skills", "core skills"]:
            current_section = "skills"

        elif line.lower() in ["work experience", "experience", "professional experience"]:
            current_section = "work_experience"

        elif line.lower() == "education":
            current_section = "education"

        elif line.lower() in ["certifications", "certification"]:
            current_section = "certifications"

        elif line.lower() == "projects":
            current_section = "projects"

        elif current_section and line:
            sections[current_section].append(line)

    return sections
if __name__ == "__main__":
    resume_path = "data/clean_resume.txt"

    resume_text = read_resume(resume_path)

    result = classify_sections(resume_text)

    print(result)
