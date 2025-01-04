#  6. Do the exercises on pages 105,106 and 107 of the book
"""
Exercise 6:
Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the
loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
"""
from colorama import Fore,init

init(autoreset=True)

number = input(f"{Fore.BLUE}Enter a number: {Fore.YELLOW}")
number_list=[]

while number!='done':
    number_list.append(number)
    number = input(f"{Fore.BLUE}Enter a number: {Fore.YELLOW}")

maximum = float(max(number_list))
minimum = float(min(number_list))

print(f"{Fore.GREEN}Maximum: {Fore.MAGENTA}{maximum}")
print(f"{Fore.GREEN}Minimum: {Fore.MAGENTA}{minimum}")