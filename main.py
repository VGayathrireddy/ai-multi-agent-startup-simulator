from fastapi import FastAPI
from agents.ideation_agent import ideation_agent
from agents.market_agent import market_agent
from agents.business_agent import business_agent
from agents.marketing_agent import marketing_agent
from agents.supervisor_agent import supervisor_agent


app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Startup Simulator Running"}

@app.get("/generate")
def generate(prompt: str):
    result = supervisor_agent(prompt)
    return result

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