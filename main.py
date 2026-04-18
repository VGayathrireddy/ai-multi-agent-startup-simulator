from fastapi import FastAPI
from agents.ideation_agent import ideation_agent
from agents.market_research_agent import market_research_agent
from agents.business_agent import business_agent
from agents.growth_strategy_agent import growth_strategy_agent
from agents.supervisor_agent import supervisor_agent

from fastapi.middleware.cors import CORSMiddleware # To allow CORS requests from frontend
from fastapi.responses import FileResponse # To send generated docx file back to frontend
from utils.formatter import format_business_plan, save_to_docx

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Startup Simulator Running"}

@app.get("/generate")
def generate(prompt: str):
    result = supervisor_agent(prompt)

    return {
        "status": "success",
        "data": result
    }

@app.get("/download")
def download(prompt: str):
    result = supervisor_agent(prompt)

    file_path = save_to_docx(result)

    return FileResponse(
        file_path,
        filename="business_plan.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

def extract_refined_idea(text: str):
    lines = text.split("\n")

    for line in lines:
        if "Refined Idea:" in line:
            # Case 1: Same line
            parts = line.split("Refined Idea:")
            if len(parts) > 1 and parts[1].strip():
                return parts[1].strip()

    for i, line in enumerate(lines):
        if "Refined Idea:" in line:
            # Case 2: Next line
            if i + 1 < len(lines):
                return lines[i + 1].strip()

    return text

# CORS middleware to allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)