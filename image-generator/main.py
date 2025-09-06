import requests
from PIL import Image
from io import BytesIO
import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

def artist(prompt):
    response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": prompt},
    )

    if response.status_code == 200 and response.headers.get("content-type", "").startswith("image"):
        return Image.open(BytesIO(response.content))
    else:
        return f"Error {response.status_code}: {response.text}"

# Gradio UI
demo = gr.Interface(
    fn=artist,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Image(type="pil", label="Generated Image"),
    title="Image Generator",
    description="generate an image using Stable Diffusion XL via Hugging Face Inference API."
)


demo.launch()

