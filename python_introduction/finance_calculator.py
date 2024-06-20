# Ask the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# simple annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate projected savings after one year with interest
projected_savings = monthly_savings * 12 * (1 + annual_interest_rate)

# Print the result
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
