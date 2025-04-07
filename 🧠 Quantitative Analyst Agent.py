import os
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools

from langchain_experimental.utilities import PythonREPL

# Set your GROQ API key
os.environ["GROQ_API_KEY"] = "___"  # <-- Replace with your actual API key

# Create a wrapper function for the LangChain REPL
repl = PythonREPL()

def run_python_repl(code: str) -> str:
    return repl.run(code)

# Add the __name__ attribute manually
run_python_repl.__name__ = "python_repl"

# Quant Analyst Agent setup
quant_agent = Agent(
    name="Quantitative Analyst",
    role="Performs statistical and quantitative analysis on financial data.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        run_python_repl,  # Custom-wrapped REPL function
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)
    ],
    instructions="Always explain calculations. Use Python for quantitative tasks. Present output with tables and visuals.",
    markdown=True
)

# Query for analysis
quant_agent.print_response("Analyze Apple's stock price trends over the last year.", stream=True)
