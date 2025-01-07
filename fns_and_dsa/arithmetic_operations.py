# Arithmentic operations

def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operations on two numbers
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation"
    