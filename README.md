CALCULATOR DOCUMENTATION

This Python script implements an interactive terminal calculator. It allows users to repeatedly perform arithmetic operations (addition, subtraction, 
multiplication, and division) on two numbers until they explicitly type 'exit' 
to quit.

1. Code Structure & Explanation

A. The `Calculator` Class
   - Encapsulates four main mathematical methods:
     * add(self, a, b): Returns the sum of a and b ($a + b$).
     * subtract(self, a, b): Returns the difference of a and b ($a - b$).
     * multiply(self, a, b): Returns the product of a and b ($a \times b$).
     * divide(self, a, b): Returns the quotient of a and b ($\frac{a}{b}$).

   - Includes input validation:
     * Raises a `TypeError` if either argument is not an `int` or `float`.
     * Raises a `ValueError` inside `divide()` if the second number is zero ($b = 0$).

B. Interactive Loop (`while True`)
   - Keeps the program running continuously so you can perform multiple calculations.
   - Prompts for inputs one by one.
   - Evaluates string inputs using `.strip().lower() == 'exit'` to safely catch variations like "Exit", " EXIT ", or "exit".
   - Immediately terminates the program via `break` when 'exit' is detected.

C. Error Handling (`try-except`)
   - Safely attempts to convert inputs to floating-point numbers (`float`).
   - Catches invalid text inputs (e.g., typing letters instead of numbers) or division-by-zero errors without crashing the main loop.

2. How to Interact with the Program

Step 1: Run the Script
   Execute the Python file in your terminal or command prompt:
   $ python calculator.py

Step 2: Input Numbers
   - You will be prompted to enter the first number:
     Enter first number (or 'exit'): 15
   - You will then be prompted to enter the second number:
     Enter second number (or 'exit'): 3

Step 3: View Results
   - The script performs all four calculations automatically and displays the results:
     --- Results ---
     Addition: 18.0
     Subtraction: 12.0
     Multiplication: 45.0
     Division: 5.0

Step 4: Repeat or Quit
   - After showing results, the prompt restarts automatically.
   - To stop the program at any time (either at the first or second prompt), type `exit`:
     Enter first number (or 'exit'): exit
     Exiting calculator. Goodbye!

3. Handling Errors During Execution
- Invalid Inputs:
  If you type non-numeric text (e.g., "hello"), the program will catch the error,
  display an error message, and prompt you again without closing:
  Error: could not convert string to float: 'hello'

- Division by Zero:
  If you enter 0 as the second number, the script safely notifies you:
  Error: Cannot divide by zero.