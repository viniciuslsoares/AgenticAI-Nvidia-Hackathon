from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import yaml
import os

load_dotenv()

# === Load agent and task configurations ===
base_dir = os.path.dirname(__file__)
config_dir = os.path.join(base_dir, "config")

with open(os.path.join(config_dir, "agents.yaml"), "r") as f:
    agents_data = yaml.safe_load(f)

with open(os.path.join(config_dir, "tasks.yaml"), "r") as f:
    tasks_data = yaml.safe_load(f)

# === Tool ===
search_tool = SerperDevTool()

# === Agent Factory ===
def create_agent(name, config):
    return Agent(
        role=config["role"],
        goal=config["goal"],
        backstory=config["backstory"],
        tools=[search_tool] if "tools" in config else [],
        verbose=True,
        memory=True
    )

# === Build agents ===
agents = {name: create_agent(name, data) for name, data in agents_data.items()}

# === Task Factory with output_key handling ===
def create_task(name, config):
    task = Task(
        description=config["description"],
        expected_output=config["expected_output"],
        agent=agents[config["agent"]],
        tools=[search_tool] if "tools" in config else [],
        output_key=name,  # ← Important fix to allow placeholder references!
        output_file=config.get("output_file")  # ✅ Enables writing to markdown
    )
    return task

# === Task execution order ===
task_sequence = [
    "sourcing_task",
    "financial_due_diligence",
    "legal_due_diligence",
    "product_analysis",
    "market_analysis",
    "final_memo"
]

# === Build tasks with correct output_keys ===
tasks = [create_task(name, tasks_data[name]) for name in task_sequence]

# === Final crew ===
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)
