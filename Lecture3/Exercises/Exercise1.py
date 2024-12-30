from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to multiply two numbers
def multiply(num1, num2):
    """
    Multiplies two numbers and returns the product.
    
    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    
    Returns:
    int or float: The product of the two numbers.
    """
    return num1 * num2

# use the function
if __name__ == "__main__":
    # Test the multiply function
    try:
        print(Fore.MAGENTA +"Enter two numbers to multiply them 🙅🏻‍♀️")
        number1 = float(input())
        number2 = float(input())
        result = multiply(number1, number2)
        print(Fore.GREEN + f"The product of {Fore.YELLOW}{number1}{Fore.GREEN} and {Fore.YELLOW}{number2}{Fore.GREEN} is: {Fore.CYAN}{result}")
    except ValueError:
        print("Error, please enter numeric input.")