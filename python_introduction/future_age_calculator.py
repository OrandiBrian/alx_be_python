#!/usr/bin/python3

"""Python script that asks the user for their urrent age and then calculates how old they wil be in a specific future year"""

# prompting for input
age = int(input("How old are you?" ))

# calculating how old user will be in 2050 assuming it is 2023
diff = 2050 - 2023
future_age = age + diff

# results
print(f"In 2050, you will be {future_age} years old.")
