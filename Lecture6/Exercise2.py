#  2. Write a program to count the number of lines in a file.
from colorama import Fore,init

file = open('Lecture6/Mohammed.txt','r')
file_lines = file.readlines()
file.close()
print(f"{Fore.GREEN}Number of lines in Mohammed file is : {Fore.MAGENTA}{len(file_lines)}")
