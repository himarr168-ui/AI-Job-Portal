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

    for line in lines:
        if "Experience" in line:
            job["experience"] = line.replace("Experience:", "").strip()

        if "Education" in line:
            job["education"] = line.replace("Education:", "").strip()

    return job

if __name__ == "__main__":
    jd_path = "data/sample_jd.txt"

    text = read_jd(jd_path)
    cleaned_text = clean_text(text)
    job=extract_job_details(text)

    print(job)
