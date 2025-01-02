# Do the exercises on pages 64 and 65 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024).

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
from colorama import Fore, init

init(autoreset=True)

max_num = None
min_num = None

while True:
    num = input(f"{Fore.BLUE}Enter number: {Fore.YELLOW}")
    
    if num.lower() == "done":
        if max_num is not None and min_num is not None:
            print(f"{Fore.MAGENTA}Maximum: {Fore.GREEN}{max_num}{Fore.MAGENTA} And Minimum: {Fore.GREEN}{min_num}{Fore.MAGENTA}")
        else:
            print(f"{Fore.MAGENTA}No valid numbers were entered.")
        break
    
    try:
        num = int(num)
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num
            
    except:
        print(f"{Fore.RED}Invalid data. Please enter a valid number.")
