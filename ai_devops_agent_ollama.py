from langchain.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# 1️⃣ Local AI Brain (NO API KEY)
llm = Ollama(
    model="mistral",
    temperature=0
)

# 2️⃣ Tool (what agent can DO)
def create_ci_workflow(input_text: str) -> str:
    return "Generated GitHub Actions workflow using Ollama!"

ci_tool = Tool(
    name="Create CI Workflow",
    func=create_ci_workflow,
    description="Generates a GitHub Actions CI/CD workflow"
)

# 3️⃣ Create Agent
agent = initialize_agent(
    tools=[ci_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4️⃣ Run Agent
goal = "Create a CI/CD workflow"
result = agent.run(goal)

print("\nRESULT:\n", result)
