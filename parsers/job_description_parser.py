def read_jd(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
def clean_text(text):
    text = " ".join(text.split())
    return text
def extract_job_details(text):
    job = {}

    lines = text.split("\n")

    job["role"] = lines[0].strip()

    skills = []
    for line in lines:
        if line.startswith("-"):
            skills.append(line.replace("-", "").strip())

    job["skills"] = skills

    for i, line in enumerate(lines):

     if "experience" in line.lower() and i + 1 < len(lines):
        job["experience"] = lines[i + 1].strip()

     elif "education" in line.lower() and i + 1 < len(lines):
        job["education"] = lines[i + 1].strip()


    return job

if __name__ == "__main__":
    jd_path = "data/sample_jd.txt"

    text = read_jd(jd_path)
    cleaned_text = clean_text(text)
    job=extract_job_details(text)

    print(job)
