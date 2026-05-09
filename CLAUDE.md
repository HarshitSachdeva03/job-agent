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
[x] Backend scaffold with /analyze endpoint
[x] Frontend form (job description + resume paste fields)
[x] n8n workflow (webhook → Claude API → response)
[x] Google Sheets logging
[x] Demo mode with pre-filled sample data

## What I'd add next
- Google Sheets integration for persistent logging (requires OAuth setup)
- User authentication
- Support for multiple AI providers (Claude, GPT, Gemini) via dropdown
- Resume PDF upload with text extraction
- Email notification when match score > 80