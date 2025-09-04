# ✈️ Airline Assistant (FlightAI)

An AI-powered **customer support assistant** for an airline called **FlightAI**.  
It provides short, courteous answers and can fetch **ticket prices** using function calling (tools).  
Built with **Gradio** + **OpenRouter** (or **Ollama** locally).

---

## 🚀 Features
- 🗨️ One-sentence, polite customer support responses  
- 🔎 Fetches real-time ticket prices via **function calling**  
- 🔧 Demonstrates how LLMs can use **tools** to enhance answers  
- 💻 Run locally or with OpenRouter API

---

## 📂 Project Structure
```bash
airline-assistant/
│── main.py # Core chatbot with tool integration
│── requirements.txt # Dependencies
│── README.md # Project documentation
└── .env # API keys
```


---

## 🛠️ Setup & Installation

1. Clone the repo and navigate to the project:
   ```bash
   git clone https://github.com/yourusername/LLM-projects.git
   cd LLM-projects/airline-assistant
 
2. Create a virtual environment & install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```
3. Add your API key in .env:
```bash
OPENAI_API_KEY=your_openrouter_key_here
```

4. Run:
```bash
python main.py
```