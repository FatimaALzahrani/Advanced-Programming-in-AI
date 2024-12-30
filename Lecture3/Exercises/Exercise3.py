from colorama import Fore, Style, init
import random

# Function to generate a random number between two given numbers
def random_between(x, y):
    """
    Generates a random number between two given numbers.
    
    Parameters:
    x (int): The lower bound.
    y (int): The upper bound.
    
    Returns:
    int: A random number between x and y, inclusive.
    """
    if x > y:
        raise ValueError("Lower bound must be less than or equal to upper bound.")
    return random.randint(x, y)


# use the function
if __name__ == "__main__":
    # Test the random_between function
    try :
        lower_bound = int(input(Fore.BLUE+"Enter lower bound : "))
        upper_bound = int(input(Fore.BLUE+"Enter upper bound : "))
        random_number = random_between(lower_bound, upper_bound)
        print(Fore.MAGENTA + f"A random number between {Fore.YELLOW}{lower_bound}{Fore.MAGENTA} and {Fore.YELLOW}{upper_bound}{Fore.MAGENTA}: {Fore.GREEN}{random_number}")
    except:
        print("Error, please enter numeric input.")
