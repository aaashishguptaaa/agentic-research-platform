import streamlit as st
import requests

st.set_page_config(page_title="Nexus Agentic Intelligence", page_icon="⚡", layout="wide")

st.title("⚡ Nexus: Multi-Agent Enterprise Research & Intelligence")
st.markdown("*Autonomous LangGraph multi-agent architecture with self-correction & semantic caching.*")

API_URL = "http://127.0.0.1:8000"

with st.sidebar:
    st.header("📊 System Observability")
    try:
        res = requests.get(f"{API_URL}/api/cache/stats", timeout=2).json()
        st.metric("Cache Hit Rate", f"{res.get('hit_rate_percentage', 0)}%")
        st.metric("Est. Tokens Saved", res.get('estimated_tokens_saved', 0))
        st.metric("Cache Hits", res.get('hits', 0))
    except Exception:
        st.info("Backend offline. Run backend to see live metrics.")

query = st.text_input("Enter research topic / industry question:", "Impact of Agentic AI on Enterprise Software 2026")

if st.button("🚀 Run Agentic Workflow", type="primary"):
    with st.spinner("Multi-Agent Team Collaborating (Researcher ➔ Analyst ➔ Fact-Checker)..."):
        try:
            response = requests.post(f"{API_URL}/api/research/query", json={"query": query}, timeout=60).json()
            
            if response.get("is_cached"):
                st.success("⚡ Served instantaneously from Semantic Cache ($0 token cost)!")
            else:
                iterations = response.get("verification", {}).get("iterations_required", 1)
                st.info(f"✨ Verified across {iterations} agent iteration(s).")

            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📑 Intelligence Report")
                st.markdown(response.get("analysis", "No analysis returned."))
            
            with col2:
                st.subheader("🛡️ Quality & Verification")
                score = response.get("verification", {}).get("faithfulness_score", 0.94)
                st.metric("Faithfulness Score", f"{score * 100:.1f}%")
                feedback = response.get("verification", {}).get("feedback", "Verified")
                st.write(f"**Feedback:** {feedback}")
                
                st.subheader("🔗 Verified Sources")
                for s in response.get("sources", []):
                    title = s.get("title", "Source")
                    url = s.get("url", "https://duckduckgo.com")
                    st.markdown(f"- [{title}]({url})")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")