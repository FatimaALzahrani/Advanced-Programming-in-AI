from colorama import Fore, Style, init
import calculator

init(autoreset=True)

def display_menu():
    print(f"{Fore.CYAN}Welcome to the Advanced Calculator!")
    print(f"{Fore.YELLOW}Available operations:")
    print(f"{Fore.GREEN}1. add        - Addition")
    print(f"{Fore.GREEN}2. subtract   - Subtraction")
    print(f"{Fore.GREEN}3. multiply   - Multiplication")
    print(f"{Fore.GREEN}4. divide     - Division")
    print(f"{Fore.GREEN}5. power      - Exponentiation (num1^num2)")
    print(f"{Fore.GREEN}6. sqrt       - Square root of num1")
    print(f"{Fore.GREEN}7. percent    - Percentage (num1 as % of num2)")
    print(f"{Fore.GREEN}8. log        - Logarithm base 10 of num1")
    print(f"{Fore.CYAN}-----------------------------------{Style.RESET_ALL}")

def get_user_input():
    try:
        display_menu()
        operation = input(f"{Fore.MAGENTA}Enter the operation: {Style.RESET_ALL}").strip().lower()
        
        if operation == "sqrt" or operation == "log":
            num1 = float(input(f"{Fore.BLUE}Enter the number: {Style.RESET_ALL}"))
            result = calculator.calculate(num1, None, operation)
        else:
            num1 = float(input(f"{Fore.BLUE}Enter the first number: {Style.RESET_ALL}"))
            num2 = float(input(f"{Fore.BLUE}Enter the second number: {Style.RESET_ALL}"))
            result = calculator.calculate(num1, num2, operation)
        
        print(f"{Fore.GREEN}The result is: {Fore.YELLOW}{result}{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter valid numbers and operation.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")

if __name__ == '__main__':
    get_user_input()
