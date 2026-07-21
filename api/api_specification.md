# ATS API Specification

## Objective

This document defines the REST APIs required for integrating the ATS AI system with backend applications.

---

## 1. Resume Upload API

### Endpoint

POST /upload-resume

### Description

Uploads a candidate resume to the ATS system.

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

## 2. Resume Parsing API

### Endpoint

POST /parse-resume

### Description

Parses the uploaded resume and extracts candidate information.

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

## 3. ATS Scoring API

### Endpoint

POST /calculate-score

### Description

Calculates the ATS score for a parsed resume.

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

## 4. Shortlisting API

### Endpoint

POST /shortlist

### Description

Generates the final candidate status based on the ATS score.

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
