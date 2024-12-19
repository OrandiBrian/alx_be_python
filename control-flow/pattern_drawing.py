"""
Script that will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asteriks (*)
"""

# user prompt
size = int(input("Enter the size of the pattern: "))
number = 1

# drawing the pattern
while number < size+1:
    for i in range(1, 5):
        print("*", end="")
    number += 1
    print()
