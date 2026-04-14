from llm.ollama_client import generate_response

def marketing_agent(idea: str):
    prompt = f"""
You are a marketing strategist.

Create a marketing and growth strategy.

Idea: {idea}

STRICT INSTRUCTIONS:
- Keep it concise
- Do NOT add extra sections
- Follow exact format

FORMAT:

Target Audience:
<answer>

Marketing Channels:
<answer>

User Acquisition Strategy:
<answer>

Growth Strategy:
<answer>
"""
    
    return generate_response(prompt)