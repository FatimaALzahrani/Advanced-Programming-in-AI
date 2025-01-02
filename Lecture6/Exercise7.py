#  5. Do the exercises on pages 89 and 90 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024

""" 
Exercise 3:  Sometimes when programmers get bored or want to have a bit of fun, they add a
harmless Easter Egg to their program. Modify the program that prompts the user
 for the file name so that it prints a funny message when the user types in the exact
 file name “na na boo boo”. The program should behave normally for all other files
 which exist and don’t exist. Here is a sample execution of the program:
"""

#  python egg.py
#  Enter the file name: mbox.txt
#  There were 1797 subject lines in mbox.txt
#  python egg.py
#  Enter the file name: missing.tyxt
#  File cannot be opened: missing.tyxt
#  python egg.py
#  Enter the file name: na na boo boo
#  NA NA BOO BOO TO YOU- You have been punkd!

#  We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.
from colorama import Fore,init,Style

init(autoreset=True)

file_name=input(f"{Fore.BLUE}Enter the file name: {Fore.YELLOW}")

try:
    with open('Lecture6/'+file_name,'r') as file:
        subject_count = sum(1 for line in file if line.startswith("Subject"))
        print(f"{Fore.GREEN}There were {Fore.MAGENTA}{subject_count}{Fore.GREEN} subject lines in {Fore.MAGENTA}{file_name}")
except FileNotFoundError:
    if(file_name=='na na boo boo'):
        print(f"{Fore.LIGHTGREEN_EX}NA NA BOO BOO TO YOU- You have been punkd!")
    else:
        print(f"{Fore.RED}File cannot be opened: {Style.DIM}{file_name}")