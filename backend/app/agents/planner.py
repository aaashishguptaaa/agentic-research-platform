from backend.app.agents.state import AgentState

def planner_agent(state: AgentState) -> dict:
    """Decomposes complex research queries into structured investigation goals."""
    query = state["query"]
    
    plan = [
        f"1. Analyze global market drivers & technology landscape for: '{query}'",
        f"2. Gather quantitative performance data, benchmarks & industry case studies",
        f"3. Identify key regulatory risks, security vulnerabilities & economic bottlenecks",
        f"4. Synthesize strategic recommendations & executive action items"
    ]
    
    return {"plan": plan}