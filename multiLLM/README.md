# 🤖 Multi-LLM Chatbot

A lightweight, modular chatbot powered by **Groq**, **OpenRouter**, and **Hugging Face** all using **free-tier models**. Built with **Gradio** for a clean UI and rapid prototyping.

---

## 🚀 Features

- 🔁 **Multi-Model Routing**: Switch between Groq, OpenRouter, and Hugging Face models
- 🧠 **Auto-Routing Ready**: Easily extend to route based on task type
- 🧪 **Free API Access**: No paid keys required—uses public/free-tier endpoints
- 🧼 **Minimal Setup**: Just one Python file and a `.env` for secrets
- 🎨 **Gradio UI**: Chat interface with dropdown model selection

---

## 🧠 Supported Models

| Provider     | Model Name                                | Use Case              |
|--------------|--------------------------------------------|------------------------|
| Groq         | `llama3-8b-8192`, `mixtral-8x7b-32768`     | Code, reasoning        |
| OpenRouter   | `mistralai/mistral-small-3.2`, `qwen-2.5`  | Summarization, coding |
| Hugging Face | `zephyr-7b-beta`                           | General chat           |

---
### Folder structure
```text
multiLLM/
├── .env                  # API keys and model configs
├── .gitignore            # Git exclusions (env, cache, etc.)
├── main.py               # Core chatbot logic + Gradio UI
├── README.md             # Project overview and usage guide
└── requirements.txt      # Python dependencies
```
---
## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/multi-llm-chatbot.git
cd multi-llm-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your `.env`
Create a `.env` file in the root directory
```bash
# Groq
GROQ_API_KEY=your_groq_key
GROQ_MODEL=llama3-8b-8192

# OpenRouter
OPENROUTER_API_KEY=your_openrouter_key
OPENROUTER_MODEL=qwen2-7b-instruct

# Hugging Face
HF_API_KEY=your_hf_key
HF_MODEL=HuggingFaceH4/zephyr-7b-beta
```

### 4. Run the app
```bash
python main.py
```


