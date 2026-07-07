import pdfplumber
from docx import Document
import os
def read_pdf(resume_path):
    text=""
    with pdfplumber.open(resume_path) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()
            if page_text:
                text+=page.extract_text()+"\n"

    return text
def read_docx(file_path):
    doc=Document(file_path)
    text=""
    for para in doc.paragraphs:
        text+=para.text+"\n"
    return text
def clean_text(text):
    #text=text.replace("\n"," ")
    text=" ".join(text.split())
    return text

def save_text(text, output_file):
    with open(output_file,"w",encoding="utf-8") as file:
        file.write(text)

if __name__=="__main__":
    resume_path="data\sampleresume.pdf"
    text=read_pdf(resume_path)
    cleaned_text=clean_text(text)
    save_text(cleaned_text,"data\clean_resume.txt")
    print("Resume parsed successfully")