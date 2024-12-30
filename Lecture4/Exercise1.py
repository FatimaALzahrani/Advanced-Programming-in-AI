# Write a loop that prints all odd numbers between 1 and 10.
from colorama import Fore,init

init(autoreset=True)

def odd_number_using_for():
    print(f"{Fore.MAGENTA}Odd numbers between 1 and 10 using {Fore.GREEN}for{Fore.MAGENTA} is : ")
    for num in range(1, 11):
        if num % 2 != 0:
            print(f"{Fore.BLUE}{num}")


def odd_number_using_while():
    print(f"{Fore.MAGENTA}Odd numbers between 1 and 10 using {Fore.GREEN}While{Fore.MAGENTA} is : ")
    num=1
    while num <= 10:
        if num % 2 != 0:
            print(f"{Fore.BLUE}{num}")
        num += 1

if __name__ == '__main__':
    odd_number_using_for()
    odd_number_using_while()