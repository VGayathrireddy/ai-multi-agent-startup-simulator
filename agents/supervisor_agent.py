from agents.ideation_agent import ideation_agent
from agents.market_research_agent import market_research_agent
from agents.business_agent import business_agent
from agents.growth_strategy_agent import growth_strategy_agent
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
    market_research_result = market_research_agent(refined_idea)
    business_result = business_agent(refined_idea)
    growth_strategy_result =growth_strategy_agent(refined_idea)

    data = {
        "refined_idea": refined_idea,
        "idea_full": clean_idea,  # ✅ use cleaned version
        "market_research": market_research_result,
        "business": business_result,
        "growth_strategy": growth_strategy_result
    }

    # 🆕 Create formatted document
    formatted = format_business_plan(data)

    save_to_docx(data)

    return data