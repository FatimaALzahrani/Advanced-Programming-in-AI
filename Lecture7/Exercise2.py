#  2. Write a program to remove duplicates from a list.
from colorama import Fore,init

init(autoreset=True)

# using set 
def with_set(list_num):
    list_uniq = list(set(list_num))
    print(f"{Fore.GREEN}List without duplicates using set : {Fore.MAGENTA}{list_uniq}")

# using loop with append
def with_loop(list_num):
    list_uniq = []
    for num in list_num:
        if num not in list_uniq:
            list_uniq.append(num)
    
    print(f"{Fore.GREEN}List without duplicates using loop & append : {Fore.MAGENTA}{list_uniq}")

# using loop with remove
def with_loop_remove(list_num):
    for num in list_num[:]:
        if list_num.count(num) > 1: 
            list_num.remove(num)
    
    print(f"{Fore.GREEN}List without duplicates using loop & remove : {Fore.MAGENTA}{list_num}")

if __name__ == '__main__':
    list_num=[11,12,67,86,12,86,11,10]
    print(f"{Fore.BLUE}Original list : {Fore.YELLOW}{list_num}")
    with_set(list_num)
    with_loop(list_num)
    with_loop_remove(list_num)