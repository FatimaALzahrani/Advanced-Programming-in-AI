# Write a program to reverse a string using slicing.
from colorama import Fore, Style

def reverse_string(string):
    # using loop
    reversed_str = ''
    str_len = len(string)-1
    while str_len>=0:
        reversed_str+=string[str_len]
        str_len-=1
    print(f"{Fore.MAGENTA}Reversed string using loop: {Fore.YELLOW}{reversed_str}")
    # using slicing
    reversed_string = string[::-1]
    print(f"{Fore.MAGENTA}Reversed string using slicing: {Fore.YELLOW}{reversed_string}")

if __name__ == '__main__':
    string = input(f"{Fore.BLUE}Enter a string: {Fore.LIGHTGREEN_EX}")
    reverse_string(string)

