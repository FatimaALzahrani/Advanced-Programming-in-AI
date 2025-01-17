# Create a set of numbers and add a new number to it.
from colorama import Fore,init,Style

init(autoreset=True)

if __name__ == '__main__':
    phone_numbers = {1234567890, 9876543210, 1122334455}
    new_phone = int(input(f"{Fore.BLUE}Enter a new phone number to add: {Fore.YELLOW}" ))
    print(f"{Fore.GREEN}Phone numbers: {Fore.MAGENTA}{phone_numbers}")
    phone_numbers.add(new_phone)
    print(f"{Fore.GREEN}Updated phone numbers: {Fore.MAGENTA}{phone_numbers}")