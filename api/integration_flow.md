# ATS Integration Flow

## Objective

This document describes the complete flow of the ATS AI system from resume upload to candidate shortlisting.

---

## System Flow

```text
Client

↓

Resume Upload

↓

Resume Parser

↓

Skill Extraction

↓

Experience Parser

↓

Education Parser

↓

Semantic Matching

↓

ATS Scoring Engine

↓

Candidate Ranking

↓

Shortlisting

↓

API Response
```

---

## Async Job Handling

The ATS processes resumes asynchronously to improve performance.

Workflow:

```text
Resume Upload

↓

Job Created

↓

Background Processing

↓

Resume Parsing

↓

ATS Scoring

↓

Candidate Ranking

↓

Status Updated (Completed)
```

---

## Error Handling

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Resume Not Found |
| 500 | Internal Server Error |

---

## Logging Standards

### INFO
- Resume uploaded successfully
- Resume parsed successfully
- ATS score generated
- Candidate shortlisted

### WARNING
- Missing optional resume fields
- Incomplete candidate information

### ERROR
- Resume upload failed
- Resume parsing failed
- ATS scoring failed
- Internal server error