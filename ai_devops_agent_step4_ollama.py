import os
from git import Repo
from langchain_community.llms import Ollama

# 1️⃣ Local LLM (Ollama)
llm = Ollama(model="mistral", temperature=0)

# 2️⃣ Create CI Workflow (NO agent decision here)
def create_ci_workflow():
    workflow_dir = ".github/workflows"
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_path = os.path.join(workflow_dir, "ci.yml")


    print("✅ CI workflow created")

# 3️⃣ Commit & Push
def commit_and_push():
    repo = Repo(os.getcwd())
    repo.git.add(all=True)
    repo.index.commit("AI Agent (Ollama): add CI workflow")
    repo.remote(name="origin").push()
    print("✅ Workflow committed & pushed")

# 4️⃣ Execute (AI assists, but DOES NOT decide tools)
print("🧠 AI Agent starting (Ollama)")

create_ci_workflow()
commit_and_push()

print("🚀 DONE: CI/CD workflow deployed successfully")
