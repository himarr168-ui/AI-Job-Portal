import re
import pdfplumber
from docx import Document
import os


def read_pdf(resume_path):
    text = ""

    try:
        with pdfplumber.open(resume_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return text


def read_docx(file_path):
    text = ""

    try:
        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print(f"Error reading DOCX: {e}")

    return text


def clean_text(text):

    # Remove unwanted special characters
    text = re.sub(r"[^\w\s@.,:/()-]", " ", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()


def save_text(text, output_file):

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)

    except Exception as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":

    resume_path = os.path.join("data", "sampleresume.pdf")

    text = read_pdf(resume_path)

    cleaned_text = clean_text(text)

    output_path = os.path.join("data", "clean_resume.txt")

    save_text(cleaned_text, output_path)

    print("Resume parsed successfully")
