import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# 1️⃣ AI Brain
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# 2️⃣ Tool: Write GitHub Actions Workflow to File
def write_github_actions_yaml(input_text: str) -> str:
    """
    Creates .github/workflows/ci.yml with a Python CI/CD workflow
    """

    workflow_dir = ".github/workflows"
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_path = os.path.join(workflow_dir, "ci.yml")

    workflow_content = f"""
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

    with open(workflow_path, "w") as file:
        file.write(workflow_content)

    return f"GitHub Actions workflow created at {workflow_path}"

tool = Tool(
    name="Write GitHub Actions Workflow",
    func=write_github_actions_yaml,
    description="Creates and saves a GitHub Actions CI/CD workflow file"
)

# 3️⃣ Create AI Agent
agent = initialize_agent(
    tools=[tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4️⃣ Run Agent
goal = "Create and save a CI/CD workflow for a Python project"

result = agent.run(goal)
print(result)
