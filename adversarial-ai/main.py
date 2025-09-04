import os
import requests
from dotenv import load_dotenv

# Load API keys
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq API endpoint
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"

def groq_chat(system_prompt, user_message):
    """Send a message to Groq LLM with a system role"""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.8
    }
    response = requests.post(GROQ_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# Define two adversarial bots
snarky_system = "You are SnarkyBot. You are sarcastic, rude, and always try to win arguments."
kind_system   = "You are KindBot. You are polite, empathetic, and always try to de-escalate arguments."

def run_debate(topic):
    print(f"\n🔥 Debate Topic: {topic}\n")

    # Round 1
    snarky_reply = groq_chat(snarky_system, topic)
    print("🤖 SnarkyBot:", snarky_reply)

    # Round 2
    kind_reply = groq_chat(kind_system, snarky_reply)
    print("😊 KindBot:", kind_reply)

    # Round 3
    snarky_reply = groq_chat(snarky_system, kind_reply)
    print("🤖 SnarkyBot:", snarky_reply)

    # Round 4
    kind_reply = groq_chat(kind_system, snarky_reply)
    print("😊 KindBot:", kind_reply)

if __name__ == "__main__":
    topic = input("Enter a debate topic: ")
    run_debate(topic)
