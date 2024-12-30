# Modify the program to handle invalid inputs gracefully using try and except.
from colorama import Fore, Style

def calculate_factorial():
    try:
        num = int(input(f"{Fore.CYAN}Enter a non-negative integer: {Style.RESET_ALL}"))
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        
        # Using for loop
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        
        print(f"{Fore.GREEN}Factorial of {num} using for loop is: {factorial}{Style.RESET_ALL}")

        # Using while loop
        factorial = 1
        i = 1
        while i <= num:
            factorial *= i
            i += 1
        
        print(f"{Fore.YELLOW}Factorial of {num} using while loop is: {factorial}{Style.RESET_ALL}")
    except ValueError as e:
        print(f"{Fore.RED}Invalid input: {e}{Style.RESET_ALL}")

calculate_factorial()
