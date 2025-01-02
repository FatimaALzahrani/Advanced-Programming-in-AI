# Do the exercises on pages 64 and 65 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024).

#   Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
#   create a function called computepay which takes two parameters (hours and rate).
from colorama import Fore, Style

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * (rate * 1.5)
            total_pay = (40 * rate) + overtime_pay
        else:
            total_pay = hours * rate
        
        return f"{Fore.GREEN}Total Pay: {total_pay}"
    except ValueError:
        return f"{Fore.RED}Invalid input. Please enter numeric values."

# Input
hours = input(f"{Fore.CYAN}Enter Hours: ")
rate = input(f"{Fore.CYAN}Enter Rate: ")
print(computepay(hours, rate))