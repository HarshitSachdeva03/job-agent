# Job Application Agent

An AI-powered tool that takes a job description and resume, then returns tailored resume bullet points, a cover letter draft, and a match score. Built with n8n for workflow orchestration and Gemini AI.

---

## How it works

```
Frontend → n8n webhook → Gemini API → parsed response → frontend display
```

The user pastes a job description and resume into the browser. The frontend POSTs to an n8n webhook, which calls the Gemini API with a structured prompt. n8n parses the JSON response and returns it to the frontend, which displays the match score, tailored bullets, and cover letter.

---

## Tech stack

- HTML / CSS / JS — single-file frontend, no frameworks
- n8n — workflow engine handling the webhook, API call, and response parsing
- Gemini 2.5 Flash — AI model via Google AI Studio API
- FastAPI — Python backend (preprocessing / health check)
- Docker — runs n8n locally

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/harshitsachdeva03/job-agent.git
   cd job-agent
   ```

2. **Create your `.env`**
   ```bash
   cp .env.example .env
   # Add your Gemini API key to .env
   ```

3. **Run n8n**
   ```bash
   docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
   ```

4. **Prepare and import the workflow**
   ```bash
   python n8n/prepare_workflow.py
   # Import n8n/Job Application Agent.ready.json into n8n at http://localhost:5678
   ```

5. **Open the frontend**
   ```
   Open frontend/index.html in your browser
   ```

---

## Screenshot

![Demo](screenshots/demo.png)

---

## Built with

Developed using [Claude Code](https://claude.ai/code) as the AI-assisted development environment.

---

## Future improvements

- Google Sheets integration for persistent logging (requires OAuth setup)
- User authentication
- Support for multiple AI providers (Claude, GPT, Gemini) via dropdown
- Resume PDF upload with text extraction
- Email notification when match score > 80
