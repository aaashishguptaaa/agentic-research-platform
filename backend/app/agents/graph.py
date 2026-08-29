from langgraph.graph import StateGraph, END
from backend.app.agents.state import AgentState
from backend.app.agents.planner import planner_agent
from backend.app.agents.researcher import research_agent
from backend.app.agents.analyzer import analysis_agent
from backend.app.agents.fact_checker import fact_checker_agent, route_next_step

def build_agent_graph():
    """Builds the 4-agent LangGraph workflow: Planner -> Researcher -> Analyst -> Fact-Checker."""
    workflow = StateGraph(AgentState)
    
    workflow.add_node("planner", planner_agent)
    workflow.add_node("researcher", research_agent)
    workflow.add_node("analyzer", analysis_agent)
    workflow.add_node("fact_checker", fact_checker_agent)
    
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "analyzer")
    workflow.add_edge("analyzer", "fact_checker")
    
    workflow.add_conditional_edges(
        "fact_checker",
        route_next_step,
        {
            "re_research": "researcher",
            "end": END
        }
    )
    
    return workflow.compile()

agent_app = build_agent_graph()