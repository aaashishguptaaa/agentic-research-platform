from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict

class AgentState(TypedDict):
    """Shared state passed between all AI agents in the graph."""
    query: str
    sources: List[Dict[str, str]]
    research_summary: str
    analysis: str
    verification_score: float
    verification_feedback: str
    iteration: int
    is_cached: bool
    final_report: Optional[Dict[str, Any]]