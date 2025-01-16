# Merge two dictionaries into one.

from colorama import Fore,init

init(autoreset=True)

personal_info = {
    "employee_id": 1,
    "full_name": "Fatimah Alzahrani",
    "age": 22,
    "email": "12fatimah.15@gmail.com"
}

work_info = {
    "position": "Software Engineer",
    "department": "Technology",
    "salary": 85000,
    "hire_date": "2025-01-16"
}


# 1. Using update() method
d1 = personal_info
d1.update(work_info)

# 2. Using | operator
d2 = personal_info | work_info

# 3. Using Dictionary Unpacking (**)
d3 = {**personal_info, **work_info}

# 4. Using a loop
d4 = personal_info
for key, value in work_info.items():
    d4[key] = value


def print_profile(employee_profile):
    print(Fore.CYAN + "=" * 30)
    for key, value in employee_profile.items():
        print(f"{Fore.GREEN}{key.replace('_', ' ').title()}: {Fore.MAGENTA}{value}")
    print(Fore.CYAN + "=" * 30)

print(Fore.YELLOW + "Using update() method:")
print_profile(d1)

print(Fore.YELLOW + "Using | operator (Python 3.9+):")
print_profile(d2)

print(Fore.YELLOW + "Using Dictionary Unpacking (**):")
print_profile(d3)

print(Fore.YELLOW + "Using a loop:")
print_profile(d4)


# From https://www.geeksforgeeks.org/python-merging-two-dictionaries/