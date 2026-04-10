from typing import Dict, List, Set
from feedback_agent.tools.keyword_extraction_tool import extract_keywords

THEME_KEYWORDS: Dict[str, Set[str]] = {
    "product_quality": {"quality", "durable", "broken", "defect", "faulty", "material", "build"},
    "customer_service": {"support", "service", "agent", "helpful", "rude", "response", "staff"},
    "delivery": {"delivery", "shipping", "courier", "late", "delay", "arrived", "package"},
    "pricing": {"price", "cost", "expensive", "cheap", "value", "discount", "refund"},
    "usability": {"easy", "difficult", "confusing", "intuitive", "interface", "navigation", "setup"},
    "performance": {"slow", "fast", "lag", "performance", "crash", "bug", "stable"},
}

def categorize_feedback(feedback: str) -> List[str]:
    """
        Categorize customer feedback into predefined themes based on parsed keywords.

        The ONLY allowed categories are:
        - product_quality
        - customer_service
        - delivery
        - pricing
        - usability
        - performance
        - other

        Args:
            feedback (str): The raw text of the customer feedback.

        Returns:
            List[str]: A list of matched predefined categories.
        """

    keywords = set(extract_keywords(feedback))
    matched_themes: List[str] = []

    for theme, theme_keywords in THEME_KEYWORDS.items():
        if keywords.intersection(theme_keywords):
            matched_themes.append(theme)

    return matched_themes if matched_themes else ["other"]
