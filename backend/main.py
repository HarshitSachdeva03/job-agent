from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Job Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    job_description: str
    resume: str


class AnalyzeResponse(BaseModel):
    bullets: list[str]
    cover_letter: str
    match_score: int
    reasoning: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(body: AnalyzeRequest):
    return AnalyzeResponse(
        bullets=[
            "Demonstrated experience aligning with core job requirements",
            "Strong technical background relevant to the role",
            "Track record of delivering results in similar environments",
        ],
        cover_letter=(
            "Dear Hiring Manager,\n\n"
            "I am excited to apply for this position. My background closely aligns "
            "with the requirements outlined in the job description, and I am confident "
            "I can contribute meaningfully to your team.\n\n"
            "Thank you for your consideration.\n\n"
            "Sincerely,\nApplicant"
        ),
        match_score=75,
        reasoning="Strong match because the resume demonstrates relevant technical skills and experience that directly correspond to the key requirements in the job description.",
    )
