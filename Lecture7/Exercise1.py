# 1. Create a list of numbers and find the largest and smallest numbers.
from colorama import Fore,init

init(autoreset=True)

# using build in function sorted
def with_sorted(list_num):
    sorted_list=sorted(list_num)

    largest = sorted_list[-1]
    smallest = sorted_list[0]
    print(f"{Fore.LIGHTBLACK_EX}Using Build-in function sorted : ")
    print(f"{Fore.GREEN}The Largest number is {Fore.MAGENTA}{largest}{Fore.GREEN}, and Smallest number is {Fore.MAGENTA}{smallest}")

# or using build in function min & max
def with_min_max(list_num):
    largest = max(list_num)
    smallest = min(list_num)
    print(f"{Fore.LIGHTBLACK_EX}Using Build-in functions min & max : ")
    print(f"{Fore.GREEN}The Largest number is {Fore.MAGENTA}{largest}{Fore.GREEN}, and Smallest number is {Fore.MAGENTA}{smallest}")

# or using loop
def with_loop(list_num):
    largest = list_num[0]
    smallest = list_num[0]
    for num in list_num:
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
    print(f"{Fore.LIGHTBLACK_EX}Using Loop : ")
    print(f"{Fore.GREEN}The Largest number is {Fore.MAGENTA}{largest}{Fore.GREEN}, and Smallest number is {Fore.MAGENTA}{smallest}")

if __name__ == '__main__':
    num_list=[5,7,0,3,8,1,12]
    print(f"{Fore.BLUE}The List is : {Fore.YELLOW}{num_list}")
    with_sorted(num_list)
    with_min_max(num_list)
    with_loop(num_list)

