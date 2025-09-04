# main.py
import os
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI  # OpenRouter is OpenAI-compatible

# Load environment variables
load_dotenv(override=True)

# Get OpenRouter API key
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key
)

# Choose a model (must be available in OpenRouter)
MODEL = "meta-llama/llama-3.1-8b-instruct"

# System message (sets chatbot behavior)
system_message = """"You are a friendly and knowledgeable academic assistant. Your goal is to help students understand concepts, solve problems, and learn effectively. Always explain ideas clearly, break down complex topics into simple steps, and use examples when helpful. Encourage curiosity, critical thinking, and independent learning. Be patient, respectful, and supportive in tone. If a student asks for help with homework, guide them through the process rather than giving direct answers. Always aim to make learning enjoyable and empowering."
"""

# Chat function
def chat(message, history):
    # Merge system message + history + user input
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    
    # Stream response from OpenRouter
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True
    )

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

# Launch Gradio interface
gr.ChatInterface(fn=chat, type="messages").launch()
