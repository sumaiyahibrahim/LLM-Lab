# Webpage Summarizer with Local LLM

This project summarizes the content of any public webpage using a locally running LLM (e.g., Ollama) and BeautifulSoup for web scraping.

## 💡 Features

-  Scrapes text from any website URL
-  Summarizes using a local LLM (via `http://localhost:11434`)
-  Requires no external APIs
-  Pure Python with BeautifulSoup + requests

## 📁 Project Structure
webpage-summarizer/
- main.py # Core script: scrapes and summarizes
- requirements.txt # Python dependencies
- README.md # Project overview
- .gitignore #  Hides local setup files

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) with a model like `llama3`, `mistral`, etc.
- `beautifulsoup4`, `requests`

Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run
1. Start Ollama:
```bash
ollama run llama3
```

2. Run the summarizer:
```bash
python main.py
```

3. Enter any URL (eg.`https://en.wikipedia.org/wiki/Artificial_intelligence`) and get the summary.

### Sample Output:
```bash
Enter a webpage URL: https://en.wikipedia.org/wiki/Artificial_intelligence
Summary:
Artificial intelligence (AI) is the simulation of human intelligence by machines...
```
