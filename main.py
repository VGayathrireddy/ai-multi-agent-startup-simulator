from fastapi import FastAPI
from agents.ideation_agent import ideation_agent
from agents.market_agent import market_agent
from agents.business_agent import business_agent
from agents.marketing_agent import marketing_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Startup Simulator Running"}

@app.get("/generate")
def generate(prompt: str):
    idea_result = ideation_agent(prompt)

    refined_idea = extract_refined_idea(idea_result)

    market_result = market_agent(refined_idea)

    business_result = business_agent(refined_idea)

    marketing_result = marketing_agent(refined_idea)

    return {
        "refined_idea": refined_idea,
        "idea_full": idea_result,
        "market": market_result,
        "business": business_result,
        "marketing": marketing_result
    }

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