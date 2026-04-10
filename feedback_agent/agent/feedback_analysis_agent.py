from autogen import ConversableAgent
from feedback_agent.tools.feedback_reader_tool import query_feedback
from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
from feedback_agent.tools.categorization_tool import categorize_feedback
from feedback_agent.tools.keyword_extraction_tool import extract_keywords
from feedback_agent.config import LLM_CONFIG

def create_feedback_analysis_agent() -> ConversableAgent:
    # define the agent
    agent = ConversableAgent(
        name="Feedback Analysis Agent",
        system_message="You are a helpful AI assistant. "
                      "You can read customer feedback using the feedback_reader tool. It will return a list of feedback, that consists of id & text. "
                      "You can also categorize the feedback into themes using the categorization tool. "
                      "You can also extract keywords from the feedback using the keyword_extraction tool. "
                      "Don't include any other text in your response. "
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    # add the tools to the agent
    agent.register_for_llm(name="feedback_reader", description="Read customer feedback")(query_feedback)
    ##agent.register_for_llm(name="sentiment_analysis", description="Analyze the sentiment of a customer feedback")(analyze_sentiment)
    agent.register_for_llm(name="categorization", description="Categorize feedback into themes")(categorize_feedback)
    agent.register_for_llm(name="keyword_extraction", description="Extract keywords from a customer feedback")(extract_keywords)

    return agent

def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="feedback_reader")(query_feedback)
    ##user_proxy.register_for_execution(name="sentiment_analysis")(analyze_sentiment)
    user_proxy.register_for_execution(name="categorization")(categorize_feedback)
    user_proxy.register_for_execution(name="keyword_extraction")(extract_keywords)
    return user_proxy


def main():
    user_proxy = create_user_proxy()
    feedback_analysis_agent = create_feedback_analysis_agent()
    user_proxy.initiate_chat(
        feedback_analysis_agent, 
        message="""
                1. Read feedback from the feedback store, using the feedback_reader tool.
                2. For each feedback item, analyze the categories using the categorization tool. 
                3. Assemble the results into a single valid JSON array. Each object in the array must ONLY contain the keys: 'id', 'text', and 'categories'.
                4. Output NOTHING but the raw JSON array. Exclude all other text, explanations, or markdown code blocks.
                
                Expected layout:
                [
                    {"id": 1, "text": "Delivery is too slow and the package arrived late.", "categories": ["delivery"]},
                    {"id": 2, "text": "The price is too expensive and the app crashes.", "categories": ["pricing"]}
                ]
                """
    )

if __name__ == "__main__":
    main()
