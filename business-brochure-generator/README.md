# 🧾 Business Brochure Generator using LLMs

Generate a professional company brochure using just a company name and website URL.  
Perfect for clients, investors, and potential recruits – powered by LLMs.

---

## 🚀 Project Overview

This tool scrapes information from a company’s website and uses a language model (LLM) to generate a high-quality, structured brochure.  
It includes sections like:

- ✅ About Us  
- ✅ Mission & Vision  
- ✅ Services or Products  
- ✅ Why Choose Us  
- ✅ Careers

Built with Python, BeautifulSoup, and OpenRouter (or your own LLaMA model), this project showcases the use of web scraping, prompt engineering, and LLMs for solving real-world business problems.

---

## 🧠 Key Features

-  Input: Company name + website URL
-  Web scraping using `BeautifulSoup`
-  Smart brochure generation via LLM (OpenRouter or local LLaMA)
-  Outputs a structured and readable brochure
-  Easy to extend into PDF, UI, or web app later

---

## 🗂️ Folder Structure
```bash
📦 business-brochure-generator/
├── 📄 app.py                 # Main script
├── 📄 scraper.py             # Website content extractor
├── 📄 brochure_generator.py  # LLM prompt + generation logic
├── 📄 requirements.txt       # Dependencies
├── 📄 README.md              # Project info
└── 📄 .gitignore             # Git ignore file
```


---

## ⚙️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/LLM-projects.git
cd LLM-projects/business-brochure-generator
```
2. **(Optional) Create a virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
```
3. **Install dependencies**:
```bash
pip install -r requirements.txt
```
4. **Add your API key**:
Open `brochure_generator.py` and replace:
```bash
"Authorization": "Bearer
YOUR_OPENROUTER_API_KEY"
```
5. **Now Run**:
```bash
python app.py
```
