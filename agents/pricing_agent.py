import json
import os

# Simulated pricing data for all 3 companies
pricing_data = {
    "HubSpot": {
        "Starter": {"price": 25, "features": ["Email Marketing", "CRM"]},
        "Professional": {"price": 800, "features": ["Automation", "Reporting", "AI Assistant"]},
    },
    "Salesforce": {
        "Starter": {"price": 30, "features": ["CRM", "Email Marketing"]},
        "Professional": {"price": 900, "features": ["Automation", "Reporting"]},
    },
    "Zoho CRM": {
        "Starter": {"price": 20, "features": ["CRM"]},
        "Professional": {"price": 400, "features": ["Reporting", "Automation"]},
    }
}

def detect_pricing_changes(company_name):
    # ✅ Always initialize changes
    changes = []

    # File to store persistent history
    history_file = f"data/{company_name}_pricing_history.json"
    
    old_data = {}
    if os.path.exists(history_file):
        with open(history_file) as f:
            old_data = json.load(f)
    
    new_data = pricing_data.get(company_name, {})

    # Compare old vs new
    for plan, values in new_data.items():
        if plan in old_data:
            if old_data[plan]["price"] != values["price"]:
                changes.append(f"Price changed for {plan}: {old_data[plan]['price']} → {values['price']}")
            old_features = set(old_data[plan]["features"])
            new_features = set(values["features"])
            for feature in new_features - old_features:
                changes.append(f"New feature added in {plan}: {feature}")

    # Save new data for next run
    os.makedirs("data", exist_ok=True)
    with open(history_file, "w") as f:
        json.dump(new_data, f, indent=2)

    return changes