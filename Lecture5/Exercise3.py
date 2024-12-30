# Extract the domain name from an email address.
from colorama import Fore, Style

def extract_domain(email):
    domain = email.split("@")[1]
    # domain = email.split('@')[-1]
    return domain

if __name__ == '__main__':
    email = input(f"{Fore.BLUE}Enter your email address : {Fore.LIGHTGREEN_EX}")
    domain = extract_domain(email)
    print(f"{Fore.MAGENTA}Extracted domain is {Fore.GREEN}{domain}")