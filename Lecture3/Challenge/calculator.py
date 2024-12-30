from colorama import Fore, Style
import math

def calculate(num1, num2, operation):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            return num1 / num2
        elif operation == "power":
            return math.pow(num1, num2)
        elif operation == "sqrt":  
            if num1 < 0:
                raise ValueError("Cannot calculate the square root of a negative number.")
            return math.sqrt(num1)
        elif operation == "percent": 
            return (num1 / num2) * 100
        elif operation == "log": 
            if num1 <= 0:
                raise ValueError("Logarithm requires a positive number.")
            return math.log10(num1)
        else:
            raise ValueError("Unknown operation.")
    except ValueError as e:
        return f"{Fore.RED}Error: {e}{Style.RESET_ALL}"
