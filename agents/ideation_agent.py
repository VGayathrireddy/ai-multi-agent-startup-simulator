from llm.ollama_client import generate_response

def ideation_agent(user_input: str):
    prompt = f"""
You are a startup idea expert.

Refine the following startup idea.

Idea: {user_input}

STRICT INSTRUCTIONS:
- Do NOT change section names
- Do NOT add extra sections
- Do NOT rename headings
- Follow EXACT format below

FORMAT:

Refined Idea:
<answer>

Problem it solves:
<answer>

Target Users:
<answer>

Unique Value Proposition:
<answer>
"""

    return generate_response(prompt)