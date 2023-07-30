try:
        num1 = int(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
except ValueError:
        print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")