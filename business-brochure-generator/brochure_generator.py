import requests

def generate_brochure(company_name, website_text):
    # Truncate if too long
    if len(website_text) > 3000:
        website_text = website_text[:3000] + "..."

    prompt = f"""
    Create a professional brochure for the company '{company_name}' using the info below:
    
    Website Content:
    {website_text}
 
    Brochure should include:
    - About Us
    - Mission & Vision
    - Services or Products
    - Why Choose Us
    - Careers or Join Us
    """

    # OpenRouter API endpoint and headers
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        res.raise_for_status()  # Raise exception if status code is not 200
        res_json = res.json()

        # Debug print the full response
        print(" LLM Response:", res_json)

        # Validate response structure
        if 'choices' not in res_json:
            raise ValueError(" 'choices' key not found in LLM response.")

        return res_json['choices'][0]['message']['content']

    except requests.exceptions.RequestException as e:
        return f"🚨 Network error: {e}"
    except ValueError as ve:
        return f"🚨 Value error: {ve}"
    except Exception as e:
        return f"🚨 Unexpected error: {e}"
