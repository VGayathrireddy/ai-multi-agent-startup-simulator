from agents.ideation_agent import ideation_agent
from agents.market_agent import market_agent
from agents.business_agent import business_agent
from agents.marketing_agent import marketing_agent
from utils.formatter import format_business_plan, save_to_docx

def extract_refined_idea(text: str):
    lines = text.split("\n")

    for line in lines:
        if "Refined Idea:" in line:
            parts = line.split("Refined Idea:")
            if len(parts) > 1 and parts[1].strip():
                return parts[1].strip()

    for i, line in enumerate(lines):
        if "Refined Idea:" in line:
            if i + 1 < len(lines):
                return lines[i + 1].strip()

    return text


def supervisor_agent(user_input: str):
    # Step 1: Ideation
    idea_result = ideation_agent(user_input)
    clean_idea = idea_result.replace("Refined Idea:", "").strip()
   
    # Step 2: Extract clean idea
    refined_idea = extract_refined_idea(idea_result)

    # Step 3: Run other agents
    market_result = market_agent(refined_idea)
    business_result = business_agent(refined_idea)
    marketing_result = marketing_agent(refined_idea)

    data = {
        "refined_idea": refined_idea,
        "idea_full": clean_idea,  # ✅ use cleaned version
        "market": market_result,
        "business": business_result,
        "marketing": marketing_result
    }

    # 🆕 Create formatted document
    formatted = format_business_plan(data)

    save_to_docx(data)

    return data