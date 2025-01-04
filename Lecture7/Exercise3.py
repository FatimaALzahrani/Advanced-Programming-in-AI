#  3. Create a list of squares for numbers 1 through 10 using list comprehension.
from colorama import Fore,init

init(autoreset=True)

list_num = [n**2 for n in range(1,11)]

print(f"{Fore.MAGENTA}{list_num}")