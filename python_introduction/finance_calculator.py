income = int(input("Enter your monthly income: "))

expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
projected savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly income: {income}.")
print(f"Your total monthly expenses: {expenses}.")
print(f"Your monthly savings are ${income - expenses}.")
print(f"Projected savings after one year, with interest, is: ${monthly_savings * 12 + (monthly_savings * 12 * 0.05)}.")