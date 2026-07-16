import re
import os
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

try:
    from parsers.resume_parser import read_pdf, clean_text
except ImportError:
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from parsers.resume_parser import read_pdf, clean_text


class WorkExperience(BaseModel):
    company_name: str
    job_title: str
    start_date: datetime
    end_date: Optional[datetime]
    is_current: bool


class ExperienceParser:

    def extract_experience(self, text: str) -> List[WorkExperience]:

        experiences = []

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        job_title = None
        company = None
        start = None
        end = None
        current = False

        for i, line in enumerate(lines):

            if line.lower() == "work experience":

                if i + 1 < len(lines):
                    job_title = lines[i + 1]

                if i + 2 < len(lines):
                    company = lines[i + 2]

                if i + 3 < len(lines):

                    duration_line = lines[i + 3]

                    match = re.search(
                        r"Duration:\s*([A-Za-z]+\s+\d{4})\s*[–-]\s*(Present|[A-Za-z]+\s+\d{4})",
                        duration_line,
                        re.IGNORECASE
                    )

                    if match:

                        start = datetime.strptime(
                            match.group(1),
                            "%B %Y"
                        )

                        if match.group(2).lower() == "present":
                            end = None
                            current = True
                        else:
                            end = datetime.strptime(
                                match.group(2),
                                "%B %Y"
                            )
                            current = False

                break

        if job_title and company and start:

            experiences.append(
                WorkExperience(
                    company_name=company,
                    job_title=job_title,
                    start_date=start,
                    end_date=end,
                    is_current=current
                )
            )

        return experiences


if __name__ == "__main__":

    parser = ExperienceParser()

    resume_path = os.path.join("data", "sampleresume.pdf")

    raw_text = read_pdf(resume_path)

    cleaned_text = clean_text(raw_text)

    experiences = parser.extract_experience(cleaned_text)

    print("\n========== EXPERIENCE REPORT ==========\n")

    if not experiences:
        print("No work experience detected.")
    else:
        for exp in experiences:
            print(exp.model_dump())