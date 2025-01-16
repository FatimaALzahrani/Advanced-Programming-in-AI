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

employee_profile = {**personal_info, **work_info}
print(Fore.CYAN+"=" * 30)
for key, value in employee_profile.items():
    print(f"{Fore.GREEN}{key.replace('_', ' ').title()}: {Fore.MAGENTA}{value}")
print(Fore.CYAN+"=" * 30)
