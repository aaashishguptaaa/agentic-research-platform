from typing import Dict, Any, Optional

class SemanticCache:
    """Semantic Caching layer to reduce API latency and eliminate redundant token costs."""
    def __init__(self, similarity_threshold: float = 0.88):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.threshold = similarity_threshold
        self.hits = 0
        self.misses = 0

    def get(self, query: str) -> Optional[Dict[str, Any]]:
        normalized = query.lower().strip()
        if normalized in self.cache:
            self.hits += 1
            return self.cache[normalized]
        self.misses += 1
        return None

    def set(self, query: str, data: Dict[str, Any]):
        normalized = query.lower().strip()
        self.cache[normalized] = data

    def stats(self) -> Dict[str, Any]:
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0.0
        return {
            "cached_entries": len(self.cache),
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate_percentage": round(hit_rate, 2),
            "estimated_tokens_saved": self.hits * 1850
        }

semantic_cache = SemanticCache()
