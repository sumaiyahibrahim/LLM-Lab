import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("llm-projects-key")
  
# Setup endpoint and headers
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# choosing the model
model = "meta-llama/llama-3-70b-instruct"

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bye!")
        break

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        reply = response.json()['choices'][0]['message']['content']
        print(f"AI: {reply}\n")
    except Exception as e:
        print("Error:", e)
        print("Full response:", response.text)
