# ATS Input / Output Schemas

## 1. Resume Upload

### Request

```json
{
    "resume_file": "resume.pdf"
}
```

### Response

```json
{
    "status": "success",
    "message": "Resume uploaded successfully"
}
```

---

## 2. Resume Parsing

### Request

```json
{
    "resume_id": "12345"
}
```

### Response

```json
{
    "skills": [],
    "experience": [],
    "education": [],
    "certifications": []
}
```

---

## 3. ATS Scoring

### Request

```json
{
    "resume_id": "12345"
}
```

### Response

```json
{
    "skill_score": 75,
    "experience_score": 33,
    "education_score": 30,
    "semantic_score": 37,
    "final_score": 50.3
}
```

---

## 4. Candidate Shortlisting

### Request

```json
{
    "resume_id": "12345"
}
```

### Response

```json
{
    "candidate_status": "Consider"
}
```
