from parsers.education_parser import AcademicProfile

def calculate_education_score(profile: AcademicProfile):
    score = 0

    for edu in profile.education:
        degree = edu.degree_type.lower()

        if "computer" in degree:
            score += 0.5

    score += min(len(profile.certifications) * 0.1, 0.5)

    return round(min(score, 1.0), 2)
