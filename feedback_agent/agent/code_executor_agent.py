from pathlib import Path

from autogen import ConversableAgent
from autogen.coding import DockerCommandLineCodeExecutor

work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)

executor = DockerCommandLineCodeExecutor(work_dir=work_dir)

code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={
        "executor": executor,
    },
    human_input_mode="NEVER",
)

def main():
    # Define a message containing a Python code block
    message_with_code = """
``````python
import math
print(sum(math.sqrt(i) for i in range(1000)))
```
"""

    response = code_executor_agent.generate_reply(
        messages=[{"content": message_with_code}]
    )

    # Print the response from the agent
    print("Response from code executor agent:")
    print(response)



if __name__ == "__main__":
    main()
