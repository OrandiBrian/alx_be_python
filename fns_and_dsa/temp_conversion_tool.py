""" script will define functions to convert temperatures between Celsius and Fahrenheit """

# variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float) -> float:
    """ function to convert temperature from Fahrenheit to Celsius """
    return ((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius: float) -> float:
    """ function to convert temperature from Celsius to Fahrenheit """
    return ((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)


while True:
    try:
        degree = float(input("Enter temperature to convert: "))
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

while True:
    temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temp.upper() == "C":
        print(f"{degree}°C is {convert_to_fahrenheit(degree)}°F")
        break
    elif temp.upper() == "F":
        print(f"{degree}°F is {convert_to_celsius(degree)}°C")
        break
    else:
        print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        continue