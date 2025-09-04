import os, requests, gradio as gr
from dotenv import load_dotenv

load_dotenv()
TIMEOUT = 120

# Model Configs
MODELS = {
    "Mistral Small 3.2": {"provider": "OpenRouter", "id": "mistralai/mistral-small-3.2-24b-instruct:free"},
    "Qwen 2.5 Coder": {"provider": "OpenRouter", "id": "qwen/qwen-2.5-coder-32b-instruct:free"},
    "LLaMA 3 8B": {"provider": "Groq", "id": "llama3-8b-8192"},         
}


def ask_openrouter(prompt, model_id):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Multi-LLM Chatbot"
    }
    data = {"model": model_id, "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}
    res = requests.post(url, headers=headers, json=data, timeout=TIMEOUT)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]

def ask_groq(prompt, model_id):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}", "Content-Type": "application/json"}
    data = {"model": model_id, "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}
    res = requests.post(url, headers=headers, json=data, timeout=TIMEOUT)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]

def ask_hf(prompt, model_id):
    url = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}
    res = requests.post(url, headers=headers, json={"inputs": prompt}, timeout=TIMEOUT)
    res.raise_for_status()
    out = res.json()
    return out[0]["generated_text"] if isinstance(out, list) else str(out.get("error", out))

def chat_fn(message, history, model_name):
    info = MODELS[model_name]
    try:
        if info["provider"] == "OpenRouter":
            return ask_openrouter(message, info["id"])
        if info["provider"] == "Groq":
            return ask_groq(message, info["id"])
        if info["provider"] == "HuggingFace":
            return ask_hf(message, info["id"])
    except Exception as e:
        return f"⚠️ {model_name} Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Multi-LLM Chatbot")
    dropdown = gr.Dropdown(list(MODELS.keys()), label="Select Model", value="LLaMA 3 8B")
    gr.ChatInterface(
        fn=chat_fn,
        type="messages",
        additional_inputs=[dropdown]
    )
demo.launch()
