from typing import List
import re

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "to", "of", "in", "on", "for",
    "with", "is", "are", "was", "were", "it", "this", "that", "i", "we",
    "you", "they", "he", "she", "at", "as", "be", "have", "has", "had",
}

def extract_keywords(text: str) -> List[str]:
    tokens = re.findall(r"[a-zA-Z]+", text.lower())
    keywords = [t for t in tokens if len(t) > 2 and t not in STOPWORDS]
    return list(dict.fromkeys(keywords))
