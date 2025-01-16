# Access and print data from a nested dictionary.
from colorama import Fore, init

init(autoreset=True)

employee_data = {
    "employee_1": {
        "name": "Fatimah Mohammed",
        "age": 22,
        "contact_info": {
            "email": "12fatimah.15@gmail.com",
            "phone": "1234567890"
        },
        "work_info": {
            "position": "Software Engineer",
            "department": "Technology",
            "salary": 85000
        }
    },
    "employee_2": {
        "name": "Mohammed Abduallah",
        "age": 50,
        "contact_info": {
            "email": "Mohammed@gmail.com",
            "phone": "1234567890"
        },
        "work_info": {
            "position": "Project Manager",
            "department": "Operations",
            "salary": 95000
        }
    }
}

for employee_key, employee in employee_data.items():
    print(Fore.YELLOW + "=" * 50)
    print(Fore.CYAN + f"{employee_key.replace('_', ' ').title()}:")
    print(Fore.GREEN + f"Name: {employee['name']}")
    print(Fore.MAGENTA + f"Email: {employee['contact_info']['email']}")
    print(Fore.BLUE + f"Position: {employee['work_info']['position']}")
    print(Fore.WHITE + f"Department: {employee['work_info']['department']}")
    print(Fore.RED + f"Salary: ${employee['work_info']['salary']:,}")
    print(Fore.YELLOW + "=" * 50)