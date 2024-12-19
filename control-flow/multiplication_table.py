"""
Script that generates and prints the multiplication table for a given number. given by the user
"""

# user prompt
number = int(input("Enter a number to see its multiplication table: "))

# loop
for i in range(1, 11):
    product = number * i 
    print(f"{number} * {i} = {product}")
