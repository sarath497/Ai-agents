
import csv

# Function to check data quality
def check_data_quality(file_name):

    # Read customer data
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Initialize variables
    missing_emails = []
    seen_ids = set()
    duplicate_ids = set()

    # Process each customer record
    for row in rows:

        customer_id = row["customer_id"]
        email = row["email"]

        # Check missing email
        if not email.strip():
            missing_emails.append(customer_id)

        # Check duplicate customer ID
        if customer_id in seen_ids:
            duplicate_ids.add(customer_id)
        else:
            seen_ids.add(customer_id)

    # Generate quality report
    report = {
        "total_records": len(rows),
        "missing_email_ids": missing_emails,
        "duplicate_customer_ids": sorted(duplicate_ids)
    }

    # Return report
    return report


# Execute the function
result = check_data_quality("customer.csv")

print("DATA QUALITY REPORT")
print("-------------------")
print("Total Records:", result["total_records"])
print("Missing Emails:", result["missing_email_ids"])
print("Duplicate IDs:", result["duplicate_customer_ids"])


import json

# Convert our quality report into JSON
report_json = json.dumps(result, indent=4)

# Define the AI instructions
system_prompt = """
You are an expert Data Quality Analyst.

Analyze the provided data quality report.

Your responsibilities:
1. Identify missing values.
2. Identify duplicate records.
3. Explain potential business impacts.
4. Recommend corrective actions.

Do not modify or delete any data.
"""

# Prepare the user request
user_prompt = f"""
Analyze this customer data quality report:

{report_json}

Provide a structured analysis.
"""

print("\nSYSTEM PROMPT:")
print(system_prompt)

print("\nUSER PROMPT:")
print(user_prompt)

