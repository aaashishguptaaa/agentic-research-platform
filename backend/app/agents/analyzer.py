import os
from google import genai
from backend.app.agents.state import AgentState

def analysis_agent(state: AgentState) -> dict:
    """Synthesizes raw intelligence into structured executive insights."""
    query = state["query"]
    summary = state["research_summary"]
    
    api_key = os.getenv("GEMINI_API_KEY", "")
    client = genai.Client(api_key=api_key) if api_key else None
    
    prompt = f"""
    You are an Elite Intelligence & Market Analyst.
    User Topic: "{query}"
    
    Raw Research Findings:
    {summary}
    
    Provide a comprehensive executive briefing with:
    1. Executive Summary
    2. Key Trends & Quantitative Findings
    3. Strategic Risks & Opportunities
    4. Actionable Next Steps
    """
    
    if client:
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )
            analysis_text = response.text
        except Exception:
            analysis_text = f"### Executive Summary for: {query}\n\n{summary}"
    else:
        analysis_text = f"### Executive Intelligence Briefing: {query}\n\n**Key Findings:**\n{summary}"

    return {"analysis": analysis_text}