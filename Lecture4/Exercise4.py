# Do the exercises on pages 64 and 65 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024).

# Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers.
#  If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.
from colorama import Fore, Style

count = 0
total = 0
print(f"{Fore.BLUE}Enter integers one by one (type 'done' to finish.){Fore.YELLOW}")
while True:
    num = input()
    if num.lower()=="done":
        average = total/count
        print(f"{Fore.MAGENTA}Total: {Fore.GREEN}{total}{Fore.MAGENTA}, Count: {Fore.GREEN}{count}{Fore.MAGENTA}, Average: {Fore.GREEN}{average}")
        break
    try:
        total+=int(num)
        count+=1
    except:
        print(f"{Fore.RED}Something went wrong, please enter an integer!{Fore.YELLOW}")