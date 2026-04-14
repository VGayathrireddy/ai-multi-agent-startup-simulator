from llm.ollama_client import generate_response

def market_agent(idea: str):
    prompt = f"""
You are a market research analyst.

Analyze the following startup idea.

Idea: {idea}

STRICT INSTRUCTIONS:
- Do NOT change section names
- Keep answers concise
- No extra explanation

FORMAT:

Market Demand:
<answer>

Target Market Size:
<answer>

Competitors:
<answer>

Market Trends:
<answer>
"""

    return generate_response(prompt)