#  4. Write a program to merge two lists without duplicates.
from colorama import Fore,init

init(autoreset=True)

# using loop and concationation
def with_loop_concat(names_list1,names_list2):
    merged_names = names_list1+names_list2
    names = []
    for name in merged_names:
        if name not in names:
            names.append(name)
    print(f"{Fore.GREEN}Merged two lists without duplicates and using loop is {Fore.MAGENTA}{names}")


# using set and extend
def with_set_extend(names1,names2):
    names1.extend(names2)
    names = list(set(names1))
    print(f"{Fore.GREEN}Merged two lists without duplicates  and using set is {Fore.MAGENTA}{names}")


if __name__ == '__main__':
    list1=['Fatimah','Shaekah','Majd','Hoor','Fatimah']
    list2=['Mohammed','Ahmed','Abdullah','Ahmed']
    print(f"{Fore.BLUE}List one is {Fore.YELLOW}{list1}")
    print(f"{Fore.BLUE}List tow is {Fore.YELLOW}{list2}")
    with_loop_concat(list1,list2)
    with_set_extend(list1,list2)

