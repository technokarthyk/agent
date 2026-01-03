import os
from git import Repo
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# 1️⃣ AI Brain
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# 2️⃣ Tool: Create GitHub Actions Workflow
def create_workflow(_: str) -> str:
    workflow_dir = ".github/workflows"
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_path = os.path.join(workflow_dir, "ci.yml")

    content = """
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
    with open(workflow_path, "w") as f:
        f.write(content)

    return "Workflow file created"

# 3️⃣ Tool: Commit & Push to GitHub
def commit_and_push(_: str) -> str:
    repo = Repo(os.getcwd())

    repo.git.add(all=True)
    repo.index.commit("AI Agent: add GitHub Actions CI/CD workflow")

    origin = repo.remote(name="origin")
    origin.push()

    return "Workflow committed and pushed to GitHub"

tools = [
    Tool(
        name="Create CI Workflow",
        func=create_workflow,
        description="Creates GitHub Actions CI/CD workflow file"
    ),
    Tool(
        name="Commit and Push",
        func=commit_and_push,
        description="Commits and pushes changes to GitHub"
    )
]

# 4️⃣ Create Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 5️⃣ Run Agent
goal = "Create a CI/CD workflow and push it to GitHub"
result = agent.run(goal)

print("\n✅ RESULT:\n", result)
