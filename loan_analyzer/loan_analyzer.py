# coding: utf-8
import csv
from pathlib import Path

# Inital list of loans
loan_costs = [500, 600, 200, 1000, 450]

# Amount of loans
number_of_loans = len(loan_costs)

# Print the number of loans from the list
print(f"There are {number_of_loans} loans in the list.")

# Total of all loans
loan_total = sum(loan_costs)

# Print the total value of the loans
print(f"The total value of loans is ${loan_total}")

# Average loan amount
average_loan = sum(loan_costs) / len(loan_costs)

# Print the average loan amount
print(f"The average loan amount is {average_loan}")

# New loan values 
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Get values of new loan
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"Future Value: {future_value}")
print(f"Remaining Months: {remaining_months}")


# Calculate present value of loan
annual_discount_rate = 0.20
present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
print(f"Present Value for the loan: {present_value}")


# Provide recommendation
cost = loan.get("loan_price")
if present_value >= cost:
    print("Yes, the loan is worth at least the cost to buy it.")
else:
    print("No, the loan is too expensive and not worth the price.")

# New loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Create present value function
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    """Calculates the present value of a loan."""
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    return present_value


present_value = calculate_present_value(
    new_loan["future_value"], new_loan["remaining_months"], 0.20
)
print(f"The present value of the loan is: {present_value}")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# Loop through all the loans and append any that cost $500 or less to a list
inexpensive_loans = []
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
print(f"The inexpensive loans are: {inexpensive_loans}")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Open the output path as a file object
with open(output_path, "w") as csvfile:
    # Create a csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")
    # Write the header to the output file
    csvwriter.writerow(header)
    # Loop through loan in the list of `inexpensive_loans`
    # and write the loan values to the csv
    for loan in inexpensive_loans:
        # Write the list of metrics to the output file
        csvwriter.writerow(loan.values())
