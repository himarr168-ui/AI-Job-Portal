from typing import List, Optional
from pydantic import BaseModel
import re

try:
    from parsers.resume_parser import read_pdf, clean_text
except ImportError:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from parsers.resume_parser import read_pdf, clean_text


class Education(BaseModel):
    degree_type: str
    field_of_study: str
    institution: str
    graduation_year: Optional[int]


class Certification(BaseModel):
    name: str
    category: str


class AcademicProfile(BaseModel):
    education: List[Education]
    certifications: List[Certification]


class EducationParser:

    def extract_education(self, text: str):

        education_list = []

        degree_match = re.search(
            r"(Bachelor of Science|B\.Sc\.?|Bachelor of Technology|B\.Tech\.?|Master of Science|M\.Sc\.?|MCA|BCA)",
            text,
            re.IGNORECASE,
        )

        degree = degree_match.group(1) if degree_match else ""

        field_match = re.search(
            r"Computer Science|Information Technology|Electronics|Mechanical|Civil|Commerce",
            text,
            re.IGNORECASE,
        )

        field = field_match.group(0) if field_match else ""

        year_match = re.search(r"(20\d{2})\s*[-–]\s*(20\d{2})", text)

        graduation_year = None
        if year_match:
            graduation_year = int(year_match.group(2))

        institution = ""

        lines = text.split("\n")

        for i, line in enumerate(lines):

            if "Education" in line:

                for j in range(i + 1, min(i + 6, len(lines))):

                    if (
                        "University" in lines[j]
                        or "College" in lines[j]
                        or "Institute" in lines[j]
                        or "UIT" in lines[j]
                    ):
                        institution = lines[j].strip()
                        break

        education_list.append(
            Education(
                degree_type=degree,
                field_of_study=field,
                institution=institution,
                graduation_year=graduation_year,
            )
        )

        return education_list

    def extract_certifications(self, text: str):

        certifications = []

        keywords = [
            "AWS",
            "Azure",
            "Google",
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
        ]

        for keyword in keywords:

            if keyword.lower() in text.lower():

                certifications.append(
                    Certification(
                        name=keyword,
                        category="Technical",
                    )
                )

        return certifications


if __name__ == "__main__":

    resume_path = "data/sampleresume.pdf"

    raw_text = read_pdf(resume_path)

    cleaned_text = clean_text(raw_text)

    parser = EducationParser()

    education = parser.extract_education(cleaned_text)

    certifications = parser.extract_certifications(cleaned_text)

    profile = AcademicProfile(
        education=education,
        certifications=certifications,
    )

    print("\n========== ACADEMIC PROFILE ==========\n")

    print(profile.model_dump_json(indent=4))

