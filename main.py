# main.py
from agents.hiring_agent import scrape_hiring
from agents.pricing_agent import detect_pricing_changes
from agents.strategy_agent import generate_strategy
from agents.report_agent import save_report

def main():
    # List of companies to process
    companies = ["HubSpot", "Salesforce", "Zoho CRM"]

    for company in companies:
        print(f"\n=== Processing {company} ===")

        # 1️⃣ Hiring Agent
        hiring_count = scrape_hiring(company)

        # 2️⃣ Pricing Agent
        pricing_changes = detect_pricing_changes(company)

        # 3️⃣ Strategy Agent
        strategy_output = generate_strategy(hiring_count, pricing_changes)

        # 4️⃣ Save Report
        save_report(hiring_count, pricing_changes, strategy_output, company_name=company)

if __name__ == "__main__":
    main()
