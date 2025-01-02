#  3. Modify the program to handle errors when the file is missing.
from colorama import Fore,init

try:
    with open('Lecture6/Mohammed.txt','r')as file:
        file_lines = file.readlines()
        print(f"{Fore.GREEN}Number of lines in Mohammed file is : {Fore.MAGENTA}{len(file_lines)}")
except FileNotFoundError:
    print(f"{Fore.RED}File is missing!")
