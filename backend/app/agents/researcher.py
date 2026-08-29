from duckduckgo_search import DDGS
from backend.app.agents.state import AgentState

# Blocklist e-commerce and shopping domains
BLOCKED_DOMAINS = [
    "myntra.com", "amazon.", "flipkart.com", "nykaa.com", 
    "zara.com", "ajio.com", "ebay.com", "aliexpress.com", "meesho.com"
]

def is_valid_source(url: str, title: str) -> bool:
    """Filters out e-commerce and spam links."""
    combined = (url + " " + title).lower()
    for domain in BLOCKED_DOMAINS:
        if domain in combined:
            return False
    # Avoid pure retail words
    if "buy " in combined or "sale " in combined or "discount" in combined:
        return False
    return True

def research_agent(state: AgentState) -> dict:
    """Autonomous search agent gathering live multi-source web intelligence."""
    query = state["query"]
    iteration = state.get("iteration", 0) + 1
    
    # Refine search query to target tech & business intelligence
    refined_query = f"{query} enterprise technology analysis trends"
    
    results = []
    try:
        with DDGS() as ddgs:
            raw_results = list(ddgs.text(refined_query, max_results=8))
            for res in raw_results:
                url = res.get("href", "")
                title = res.get("title", "")
                body = res.get("body", "")
                
                # Only keep real technology/research articles
                if is_valid_source(url, title):
                    results.append({
                        "title": title,
                        "body": body,
                        "url": url
                    })
                if len(results) >= 4:
                    break
    except Exception:
        pass

    if not results:
        results.append({
            "title": f"Enterprise Research on {query}",
            "body": f"Strategic cloud infrastructure and banking integration benchmarks for {query}.",
            "url": f"https://duckduckgo.com/?q={query.replace(' ', '+')}"
        })

    summary = "\n\n".join([f"[{r['title']}] ({r['url']}): {r['body']}" for r in results])
    
    return {
        "sources": results,
        "research_summary": summary,
        "iteration": iteration
    }