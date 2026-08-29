from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict

class AgentState(TypedDict):
    """Shared memory passed across the multi-agent graph."""
    query: str
    plan: List[str]
    sources: List[Dict[str, str]]
    research_summary: str
    analysis: str
    verification_score: float
    verification_feedback: str
    iteration: int
    is_cached: bool
    final_report: Optional[Dict[str, Any]]