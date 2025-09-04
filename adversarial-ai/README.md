# 🤖 Adversarial AI Debate
An AI-powered debate simulator where two contrasting bots argue over a topic:

- SnarkyBot 😏 → sarcastic, rude, and always trying to win arguments.

- KindBot 😊 → polite, empathetic, and focused on de-escalation.

The bots take turns responding to each other using Groq’s free LLM API.

## 📂 Project Structure
```bash
adversarial_ai/
│── main.py            # Main script to run debate
│── requirements.txt   # Dependencies
│── .env               # API key (not committed to GitHub)
│── README.md          # Project documentation
```

## ⚙️ Setup Instructions
1. Clone the repo (inside `llm-projects`):
```bash
git clone <your-repo-url>
cd adversarial_ai
```
2. Create & activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Add your Groq API key to a .env file:
```bash
GROQ_API_KEY=your_api_key_here
```

## ▶️ Run the Debate
```bash
python main.py
```
Enter any debate topic, for example:
```bash
Enter a debate topic: Should AI replace teachers?
```
## ✅ Sample Output
```bash
🔥 Debate Topic: Should AI replace teachers?

🤖 SnarkyBot: Obviously yes, AI doesn’t take coffee breaks or complain.
😊 KindBot: But teachers provide emotional support and mentorship that AI cannot replace.
🤖 SnarkyBot: Emotional support? That’s just therapy disguised as education.
😊 KindBot: Respectfully, human connection is essential for real learning.
```