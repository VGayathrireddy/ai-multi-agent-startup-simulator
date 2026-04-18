from typing import TypedDict
from langgraph.graph import StateGraph

# Import agents
from agents.ideation_agent import ideation_agent
from agents.market_research_agent import market_research_agent
from agents.business_agent import business_agent
from agents.growth_strategy_agent import growth_strategy_agent


# -----------------------------
# STATE (Shared Memory)
# -----------------------------
class GraphState(TypedDict):
    input: str
    refined_idea: str
    idea_full: str
    market_research: str
    business: str
    growth_strategy: str
    final_output: str


# -----------------------------
# HELPER
# -----------------------------
def extract_refined_idea(text: str):
    lines = text.split("\n")

    for line in lines:
        if "Refined Idea:" in line:
            parts = line.split("Refined Idea:")
            if len(parts) > 1 and parts[1].strip():
                return parts[1].strip()

    for i, line in enumerate(lines):
        if "Refined Idea:" in line and i + 1 < len(lines):
            return lines[i + 1].strip()

    return text


# -----------------------------
# NODES
# -----------------------------

def ideation_node(state: GraphState):
    result = ideation_agent(state["input"])

    refined = extract_refined_idea(result)
    clean = result.replace("Refined Idea:", "").strip()

    return {
        "refined_idea": refined,
        "idea_full": clean
    }


def market_research_node(state: GraphState):
    result = market_research_agent(state["refined_idea"])
    return {"market_research": result}


def business_node(state: GraphState):
    result = business_agent(state["refined_idea"])
    return {"business": result}


def growth_strategy_node(state: GraphState):
    result = growth_strategy_agent(state["refined_idea"])
    return {"growth_strategy": result}


def final_node(state: GraphState):
    output = f"""
================ BUSINESS PLAN ================

IDEA:
{state['idea_full']}

----------------------------------------------

MARKET ANALYSIS:
{state['market_research']}

----------------------------------------------

BUSINESS MODEL:
{state['business']}

----------------------------------------------

GROWTH STRATEGY:
{state['growth_strategy']}

==============================================
"""
    return {"final_output": output}


# -----------------------------
# BUILD GRAPH
# -----------------------------
workflow = StateGraph(GraphState)

# Add nodes
workflow.add_node("ideation", ideation_node)
workflow.add_node("market_research", market_research_node)
workflow.add_node("business", business_node)
workflow.add_node("growth_strategy", growth_strategy_node)
workflow.add_node("final", final_node)

# Entry
workflow.set_entry_point("ideation")

# Flow
workflow.add_edge("ideation", "market_research")
workflow.add_edge("ideation", "business")
workflow.add_edge("ideation", "growth_strategy")

workflow.add_edge("market_research", "final")
workflow.add_edge("business", "final")
workflow.add_edge("growth_strategy", "final")

# Compile
app_graph = workflow.compile()