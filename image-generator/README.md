# Pop-Art Generator
Generate vibrant, pop-art style images of any city using Stable Diffusion XL via Hugging Face’s Inference API—wrapped in a Gradio UI for instant interaction.


### 🚀 Features
- Text-to-image generation for any city or concept
- Powered by Hugging Face Inference API (no GPU required)
- Interactive Gradio interface
- Secure token management via `.env`
- Minimal dependencies for reproducibility

### 📁 Project Structure
```bash
image-generator/
├── main.py              # Core logic and Gradio UI
├── .env                 # API key
├── requirements.txt     # dependency list
├── .gitignore           # Ignores venv, .env, and other artifacts
└── README.md            
```

### 🧑‍💻 Setup Instructions
1. Clone the repo
```bash
git clone https://github.com/sumaiyahibrahim/image-generator.git
cd image-generator
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your Hugging Face token to `.env`
Create a `.env` file
```bash
HF_TOKEN=hf_your_token_here
```

5. Run
```bash
python main.py
```




