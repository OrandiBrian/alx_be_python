"""
A calculator that will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using Match Case and display the result
"""

# asking for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# initializing result
result = 0

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num1 > 0 and num2 > 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
