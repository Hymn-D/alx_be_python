income = float(input("Enter your monthly income: "))

expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
projected savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print results
print(f"Your monthly savings are ${income - expenses}.")
print(f"Projected savings after one year, with interest, is: ${monthly_savings * 12 + (monthly_savings * 12 * 0.05)}.")