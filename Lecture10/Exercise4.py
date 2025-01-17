# Create two sets and check if one is a subset of the other.

from colorama import Fore, Style

# Create two sets
set_a = {"Laptop", "Notebook", "Pen"}
set_b = {"Laptop", "Notebook", "Pen", "Tablet", "Phone"}

print(f"{Fore.LIGHTBLUE_EX}Set A : {Fore.LIGHTYELLOW_EX}{set_a}")
print(f"{Fore.LIGHTBLUE_EX}Set B : {Fore.LIGHTYELLOW_EX}{set_b}")

# Check if one set is a subset of the other
if set_a.issubset(set_b):
    print(Fore.GREEN + "Set A is a subset of Set B." + Style.RESET_ALL)
else:
    print(Fore.RED + "Set A is NOT a subset of Set B." + Style.RESET_ALL)

if set_b.issubset(set_a):
    print(Fore.GREEN + "Set B is a subset of Set A." + Style.RESET_ALL)
else:
    print(Fore.RED + "Set B is NOT a subset of Set A." + Style.RESET_ALL)
