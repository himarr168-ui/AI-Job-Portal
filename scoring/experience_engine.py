from datetime import datetime
from typing import List
from parsers.experience_parser import WorkExperience


class ExperienceEngine:

    def calculate_total_experience(self, experiences: List[WorkExperience]) -> int:
        """Calculate total experience in months."""
        total_months = 0

        for exp in experiences:
            end_date = exp.end_date if exp.end_date else datetime.now()

            months = (
                (end_date.year - exp.start_date.year) * 12
                + (end_date.month - exp.start_date.month)
            )

            if months > 0:
                total_months += months

        return total_months

    def detect_gaps(self, experiences: List[WorkExperience]):
        """Detect employment gaps."""
        gaps = []

        experiences = sorted(experiences, key=lambda x: x.start_date)

        for i in range(1, len(experiences)):
            previous = experiences[i - 1]
            current = experiences[i]

            if previous.end_date:
                gap = (current.start_date - previous.end_date).days

                if gap > 30:
                    gaps.append({
                        "after_company": previous.company_name,
                        "before_company": current.company_name,
                        "gap_days": gap
                    })

        return gaps

    def detect_overlaps(self, experiences: List[WorkExperience]):
        """Detect overlapping jobs."""
        overlaps = []

        experiences = sorted(experiences, key=lambda x: x.start_date)

        for i in range(1, len(experiences)):
            previous = experiences[i - 1]
            current = experiences[i]

            if previous.end_date and current.start_date < previous.end_date:
                overlaps.append({
                    "company_1": previous.company_name,
                    "company_2": current.company_name
                })

        return overlaps

    def calculate_relevance_score(
        self,
        experiences: List[WorkExperience],
        required_roles: List[str]
    ) -> float:
        """Simple role relevance score."""

        if not experiences:
            return 0.0

        score = 0

        for exp in experiences:
            for role in required_roles:
                if role.lower() in exp.job_title.lower():
                    score += 1
                    break

        return round(score / len(required_roles), 2)
