# 1. Write a program to read and print the contents of a text file.
from colorama import Fore,init

init(autoreset=True)

print(f"{Fore.BLUE}Using open & close :")
file = open('Lecture6/Mohammed.txt','r')
print(f"{Fore.MAGENTA}{file.read()}")
file.close()

print(f"{Fore.BLUE}Using with :")
with open('Lecture6/Mohammed.txt','r') as file:
    print(f"{Fore.MAGENTA}{file.read()}")