import ollama
import requests
from bs4 import BeautifulSoup

MODEL_NAME = "llama3.2:latest"

def summarize_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Handle non-200 HTTP responses

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        if len(text) > 3000:
            text = text[:3000]  # avoid overloading model

        prompt = f"Summarize this webpage content:\n\n{text}"
        llm_response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        return llm_response['message']['content']

    except requests.exceptions.RequestException as req_err:
        return f"Network error: {req_err}"
    except Exception as e:
        return f"Error: {e}"


#  Main interaction loop
while True:
    user_input = input("\nYou (type 'summarize <url>' or 'exit'): ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print(" Bye!")
        break

    if user_input.startswith("summarize "):
        url = user_input.split("summarize ", 1)[1].strip()
        result = summarize_webpage(url)
        print("\n🧠 Summary:\n", result)
    else:
        try:
            chat_response = ollama.chat(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": user_input}]
            ) 
            print("\n AI:", chat_response['message']['content'])
        except Exception as e:
            print("Error:", e)
 