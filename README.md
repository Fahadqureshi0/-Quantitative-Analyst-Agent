
# Quantitative Analyst Agent 🤖📊

This repository contains a **Quantitative Analyst AI Agent** built using the **Groq** AI model, **LangChain's Python REPL**, and **Yahoo Finance** data tools. The agent performs advanced statistical and quantitative analysis on financial data such as stock price trends, moving averages, and volatility. The output is displayed in readable tables and visual formats, helping financial analysts, data scientists, and anyone involved in quantitative finance. 📈

## Features 🌟

- **Groq AI Model**: Uses Groq's powerful model to interpret and process complex financial data. 🤖
- **LangChain Python REPL**: Executes custom Python code to perform quantitative tasks such as statistical analysis, regression, and visualizations. 🧑‍💻
- **Yahoo Finance Integration**: Fetches real-time financial data, including stock prices, analyst recommendations, and company information. 💹
- **Dynamic Query Processing**: The agent answers questions about financial data and generates insights based on real-time stock performance. 💬
- **Visual and Tabular Outputs**: Results are presented in tables and visual charts for easy analysis and interpretation. 📊📉

## Installation ⚙️

To use this Quantitative Analyst Agent, you need **Python 3.8+** and the required dependencies.

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/quantitative-analyst-agent.git
cd quantitative-analyst-agent
```

### 2. Create a virtual environment:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage 🚀

### 1. Set your **GROQ API Key** 🔑:

Ensure you have a valid **Groq API Key** and set it as an environment variable before running the script:

- **Windows**:
  ```bash
  set GROQ_API_KEY="your_api_key_here"
  ```
- **Mac/Linux**:
  ```bash
  export GROQ_API_KEY="your_api_key_here"
  ```

### 2. Run the agent 💻:

The agent will process financial queries and return the results with real-time data fetched from Yahoo Finance and run statistical analysis using Python.

```bash
python quantitative_analyst_agent.py
```

### 3. Query the agent 📈:

You can ask the agent to analyze financial data by modifying the query in the script, such as:

```
quant_agent.print_response("Analyze Apple's stock price trends over the last year.", stream=True)
```

The agent will provide insights on Apple's stock price trends, including volatility, moving averages, and any other relevant financial data. 📊

## Libraries Used 📚

This project uses the following libraries:

- **agno**: For building the agent and integrating with the Groq AI model. 🤖
- **langchain_experimental**: For the LangChain Python REPL to execute Python code for statistical tasks. 🧑‍💻
- **yfinance**: To fetch stock prices, company information, and analyst recommendations from Yahoo Finance. 💹

## Contribution 🤝

Feel free to fork this repository and create pull requests to improve it. If you encounter any issues or have suggestions, please open an issue on GitHub. 💬

### To Contribute 🛠️:

1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature-branch`) 🌱
3. Commit your changes (`git commit -am 'Add new feature'`) ✍️
4. Push to the branch (`git push origin feature-branch`) 🚀
5. Create a new Pull Request (PR) 🔄

---
