# agents/hiring_agent.py
import requests

def scrape_hiring(company_name):
    print(f"Scraping hiring data for {company_name}...")
    
    # Map company to careers URL
    urls = {
        "HubSpot": "https://www.hubspot.com/careers",
        "Salesforce": "https://www.salesforce.com/company/careers/",
        "Zoho CRM": "https://www.zoho.com/careers.html"
    }
    
    url = urls.get(company_name)
    if not url:
        print("URL not found for company. Returning 0.")
        return 0
    
    response = requests.get(url)
    print("Status Code:", response.status_code)
    
    text = response.text.lower()
    sales_keywords = ["sales", "account executive", "business development"]
    
    sales_count = 0
    for keyword in sales_keywords:
        sales_count += text.count(keyword)
    
    print(f"{company_name} Sales-related mentions:", sales_count)
    return sales_count