# Remove all duplicates from a list using a set.
from colorama import Fore, Style

purchases = ["Apple", "Orange", "Apple", "Banana", "Orange", "Grapes"]
unique_purchases = list(set(purchases))
print(f"{Fore.GREEN}Original purchases list: {Fore.MAGENTA}{purchases}")
print(f"{Fore.GREEN}Unique purchases: {Fore.MAGENTA}{unique_purchases}")