#Task
#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

def calculator():
    print("Welcome to the Simple Calculator!")

    # Get the user's input for the numbers and operation desired
    try:
        Number_1 = float(input("Please enter the first number: "))
        Number_2 = float(input("Please enter the second number: "))
        Operator = input("Please enter the mathematical operation you would wish to perform. Choices are +, -, /, *").strip()

        # Perform the operation
        if Operator == "+":
            result = Number_1 + Number_2
            print(f"{Number_1} + {Number_2} = {result}")
        elif Operator == "-":
            result = Number_1 - Number_2
            print(f"{Number_1} - {Number_2} = {result}")
        elif Operator == "*":
            result = Number_1 * Number_2
            print(f"{Number_1} * {Number_2} = {result}")
        elif Operator == "/":
            if Number_2 != 0:
                result = Number_1 / Number_2
                print(f"{Number_1} / {Number_2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif Operator == "%":
            if Number_2 != 0:
                result = Number_1 % Number_2
                print(f"{Number_1} % {Number_2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif Operator == "//":
            if Number_2 != 0:
                result = Number_1 // Number_2
                print(f"{Number_1} // {Number_2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter one of +, -, *, /, %, or //.")

    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

# Run the calculator
if __name__ == "__main__":
    calculator()
