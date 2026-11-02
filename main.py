
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
