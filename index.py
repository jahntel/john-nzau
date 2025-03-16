# Basic Calculator Program

# Prompt the user for inputs
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the desired operation
if operation == "+":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "-":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == "*":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "/":
    if number2 != 0:  # Check to prevent division by zero
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

# End of program
