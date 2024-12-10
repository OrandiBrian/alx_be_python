#!/usr/bin/python3

"""
Python script that calculates the user's monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest's effect on savings
"""

# prompting user for monthly income
monthly_income = int(input("What is your monthly income? "))

# prompting for total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# monthly savings calculations
monthly_savings = monthly_income - monthly_expenses

# projected annual savings
interest = 0.05
months = 12
projected_savings = monthly_savings * months + (monthly_savings * months * interest)

# results
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savigns after one year, with interest, is: ${projected_savings:.0f}.")
