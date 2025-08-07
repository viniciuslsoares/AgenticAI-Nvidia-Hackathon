# Nvidia Hackathon Crew

Welcome to the NvidiaHackathon Crew project, powered by [crewAI](https://crewai.com). 

This project was built during a Hackathon given by Jomar Silva, from NVIDIA, on SECOMP2025.

The main goal of this crew is to help you find a startup in a given sector, analyse it in finalcial, marketing, legal and product wise and give you an investment hint about its finding.

Nvidia NIM and LLM model is used, also SERPER API for online and updated data search. 

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

Follow the steps bellow to install and run this crew:

*It is recommended to run into a virtual environment
```bash
python -m venv .venv
```

Then, install the dependencies:
```bash
pip install uv

uv tool install crewai 

uv tool update-shell

crewai install
```

Now you're all set up

*If any help is needed with the instalation, vist: https://docs.crewai.com/en/installation

### Customizing
Add your API keys to .env file:

```bash
MODEL=nvidia_nim/nvidia/llama-3.1-nemotron-70b-instruct
NVIDIA_NIM_API_KEY="NVIDIA_KEY"
SERPER_API_KEY="SERPER_KEY"
```
Use these links: 
- https://serper.dev
- https://build.nvidia.com

## Running the Project

If everything is set up, just run

```bash
python -m nvidia_hackathon.main
```

This command initializes the nvidia_hackathon Crew, assembling the agents and assigning them tasks as in the config files. This crew generates a set of reports for the found 

## Venture Capital Analyst Crew 
This CrewAI project simulates a sophisticated, multi-layered investment analysis process of a Venture Capital fund. Given a specific market sector, the crew identifies a promising startup, conducts in-depth due diligence through specialized teams, and produces a final investment memorandum with a clear "INVEST" or "DO NOT INVEST" recommendation.

How It Works
The workflow is designed to mirror a real-world VC's decision-making funnel, divided into three distinct stages:

1. Sourcing
Agent: Analista de Sourcing

Objective: Scans the market to identify a single, high-potential startup within the user-defined sector. This agent acts as the "olheiro" of the fund, finding the initial lead.

2. Parallel Due Diligence
Once a target company is identified, two specialized teams work in parallel to perform a comprehensive analysis:

A. Financial & Legal Diligence Team
Agents: Investigador Financeiro & Analista Jurídico e de Compliance

Objective: This team scrutinizes the target's financial health, including funding rounds, valuation, and revenue estimates. Simultaneously, it investigates the corporate structure, potential legal risks, and regulatory compliance, flagging any potential red flags.

B. Product & Market Analysis Team
Agents: Especialista de Produto e Tecnologia & Estrategista de Mercado e Concorrência

Objective: This team evaluates the core product's technical viability, scalability, and competitive differentiation. It also maps the market size, analyzes the competitive landscape, and defines the target's unique value proposition.

3. Final Decision
Agent: Sócio Diretor de Investimentos

Objective: This is the final analyst. This agent receives the comprehensive reports from both due diligence teams. Their role is to synthesize all the financial, legal, product, and market data into a single, coherent investment thesis. The final output is a professional investment memorandum that weighs all the pros and cons and concludes with a decisive recommendation.
