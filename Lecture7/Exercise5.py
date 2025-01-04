#  5. How to remove more than one element in a list (see p.95).
#by use del with a slice index
from colorama import Fore,init

init(autoreset=True)

names = ['Ahmed', 'Mohammed', 'Abduallah', 'Fatimah']
print(f'{Fore.BLUE}Original list is : {Fore.YELLOW}{names}')
del names[1:3]
print(f"{Fore.GREEN}List after del 1:3 : {Fore.MAGENTA}{names}")
