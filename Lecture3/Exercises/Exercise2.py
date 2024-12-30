from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to check if a number is even
def is_even(n):
    """
    Checks if a number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is even, False if odd.
    """
    return n % 2 == 0


# use the function
if __name__ == "__main__":
    # Test the is_even function
    try:
        number = int(input(Fore.GREEN +"Enter the verification number to see if is even : "))
        if is_even(number):
            print(Fore.BLUE + f"{number} is even.")
        else:
            print(Fore.RED + f"{number} is odd.")
    except ValueError:
        print("Error, please enter numeric input.")