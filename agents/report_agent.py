from datetime import datetime

def save_report(hiring_count, pricing_changes, strategy_output, company_name="Unknown"):
    filename = "daily_sales_report.txt"

    with open(filename, "a") as f:
        f.write("\n==============================\n")
        f.write(f"Report generated at {datetime.now()} for {company_name}\n\n")
        f.write(f"Hiring Signal Count: {hiring_count}\n\n")
        f.write("Pricing Changes:\n")
        if pricing_changes:
            for change in pricing_changes:
                f.write(f"- {change}\n")
        else:
            f.write("No pricing changes detected.\n")
        f.write("\nStrategy Recommendations:\n")
        for line in strategy_output:
            f.write(f"- {line}\n")
        f.write("\n")

    print(f"Report saved successfully for {company_name}.")