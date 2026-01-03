# Import required classes
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# 1️⃣ AI Brain (LLM)
llm = ChatOpenAI(
    model="gpt-4o-mini",  # lightweight + cheap
    temperature=0
)

# 2️⃣ Tool (What agent can DO)
def generate_github_actions_yaml(input_text: str) -> str:
    """
    This tool generates a GitHub Actions CI/CD YAML
    """
    return f"""
name: Python CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
"""

tool = Tool(
    name="Generate GitHub Actions Workflow",
    func=generate_github_actions_yaml,
    description="Creates a GitHub Actions CI/CD workflow for a Python project"
)

# 3️⃣ Create the AI Agent
agent = initialize_agent(
    tools=[tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4️⃣ Run the Agent (GOAL)
goal = "Create a CI/CD pipeline for a Python application using GitHub Actions"

result = agent.run(goal)

print("\n--- GENERATED CI/CD WORKFLOW ---\n")
print(result)
