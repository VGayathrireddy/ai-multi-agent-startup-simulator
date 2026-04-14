from llm.ollama_client import generate_response

def business_agent(idea: str):
    prompt = f"""
You are a business strategist.

Create a business model.

Idea: {idea}

STRICT INSTRUCTIONS:
- Do NOT add titles
- Do NOT rename sections
- Only follow format below

FORMAT:

Revenue Streams:
<answer>

Pricing Strategy:
<answer>

Cost Structure:
<answer>

Key Partnerships:
<answer>
"""

    return generate_response(prompt)