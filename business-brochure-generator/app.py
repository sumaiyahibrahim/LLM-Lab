from scraper import scrape_website
from brochure_generator import generate_brochure

if __name__ == "__main__":
    company_name = input("Enter company name: ")
    website_url = input("Enter website URL: ")

    print("\n Scraping website...")
    website_text = scrape_website(website_url)

    print("\n Generating brochure using LLM...")
    brochure = generate_brochure(company_name, website_text)

    print("\n BROCHURE:")
    print(brochure)
