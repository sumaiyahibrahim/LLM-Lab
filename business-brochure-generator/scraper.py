import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Basic extraction of visible text
    paragraphs = soup.find_all('p')
    text_content = ' '.join([para.get_text() for para in paragraphs])
    return text_content[:3000]  # limit to first 3000 chars for token control