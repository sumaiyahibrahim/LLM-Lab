# studentAssist - Academic Assistant Bot

An interactive chatbot powered by **OpenRouter** (OpenAI-compatible API) and **Gradio**, designed to act as a **friendly and knowledgeable academic assistant**.  
The bot helps students **understand concepts, solve problems, and learn effectively** by breaking down complex ideas into simple steps, using examples, and encouraging curiosity.  

---

## ✨ Features
- 🤖 **LLM-powered chatbot** using OpenRouter models (e.g., `openrouter/llama-3-70b-instruct`).
- 🎓 **Academic persona**:
  - Explains concepts clearly.
  - Guides students through problems instead of giving direct answers.
  - Encourages independent learning and critical thinking.
- 🌐 **Gradio web interface** for easy interaction.
- 🔑 **Environment variable support** via `.env`.

---

## 📂 Project Structure
```bash
studentAssist/
│── main.py # Main chatbot script
│── .env # Stores API key 
│── .gitignore # Ignores venv and sensitive files
│── venv/ # Virtual environment 
│── requirements.txt # contains python dependencies required to run the project.
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/conversationalBot.git
cd conversationalBot
```
### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
# On Windows (PowerShell)
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your OpenRouter API key
Create a file named `.env` in the project root:
```bash
OPENROUTER_API_KEY=your_api_key_here
```

### 5️⃣ Run the chatbot
```bash
python main.py
```