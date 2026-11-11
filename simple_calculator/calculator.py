class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return a - b

    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return a * b

    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Instantiate the calculator class
calc = Calculator()
print("Welcome to the Calculator! Type 'exit' at any time to quit.\n")

while True:
    # Get first number or check for exit
    user_input1 = input("Enter first number (or 'exit'): ")
    if user_input1.strip().lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    # Get second number or check for exit
    user_input2 = input("Enter second number (or 'exit'): ")
    if user_input2.strip().lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    try:
        num1 = float(user_input1)
        num2 = float(user_input2)
        
        # Perform calculations
        addition = calc.add(num1, num2)
        subtraction = calc.subtract(num1, num2)
        multiplication = calc.multiply(num1, num2)
        division = calc.divide(num1, num2)

        # Output results
        print("\n--- Results ---")
        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")
        print("-" * 15 + "\n")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")