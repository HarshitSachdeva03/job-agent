# Job Application Agent

## What this project is
An AI-powered tool that takes a job description and a resume, then returns:
1. Tailored resume bullet points for that specific role
2. A short cover letter draft
3. A match score (0-100) with brief reasoning

## Tech stack
- Backend: FastAPI (Python)
- Frontend: Plain HTML + vanilla JS (no frameworks)
- Orchestration: n8n (handles webhook, Claude API call, Google Sheets logging)
- AI: Claude API via n8n HTTP node

## Architecture
The frontend sends a POST to n8n's webhook URL.
n8n calls the Claude API and returns the response.
n8n also logs each submission to Google Sheets.
The backend (FastAPI) serves the frontend and may handle preprocessing.

## Coding conventions
- Python: keep it simple, no unnecessary abstractions
- Comments on anything non-obvious
- All API keys go in .env, never hardcoded
- Keep frontend in a single index.html file for now

## Current status
[ ] Backend scaffold with /analyze endpoint
[ ] Frontend form (job description + resume paste fields)
[ ] n8n workflow (webhook → Claude API → response)
[ ] Google Sheets logging
[ ] Demo mode with pre-filled sample data