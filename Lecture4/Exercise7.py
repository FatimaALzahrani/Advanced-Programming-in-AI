# Do the exercises on pages 64 and 65 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024).

# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a string.
from colorama import Fore, Style

def computegrade(score):
    try:
        score = float(score)
        if score > 1.0 or score < 0.0:
            return f"{Fore.RED}Bad score"
        elif score >= 0.9:
            return f"{Fore.GREEN}A"
        elif score >= 0.8:
            return f"{Fore.GREEN}B"
        elif score >= 0.7:
            return f"{Fore.YELLOW}C"
        elif score >= 0.6:
            return f"{Fore.YELLOW}D"
        else:
            return f"{Fore.RED}F"
    except ValueError:
        return f"{Fore.RED}Bad score"

# Input and Testing
while True:
    user_input = input(f"{Fore.CYAN}Enter score (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    print(computegrade(user_input))