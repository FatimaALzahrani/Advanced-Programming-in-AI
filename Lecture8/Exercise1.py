#  Create a dictionary representing a student's data (name, age, subjects).

from colorama import Fore,init,Style

init(autoreset=True)

def students_info():
    students = {'1':{'name':'Fatimah Alzahrani','age':22,'subjects':['Advanced Programming in AI','Advanced Statistics and Probability']},
                '2':{'name':'Ahmed Alzahrani','age':9,'subjects':['Math','Sciences','Artistic']},
                '3':{'name':'Majd Alzahrani','age':22,'subjects':['Data visualization','Object Oriented Programming','Robots']}}
    return students

if __name__ == '__main__':
    students = students_info()
    for student_id, student_data in students.items():
        print(Fore.YELLOW + f"{Style.BRIGHT}Student ID: {Style.NORMAL}{student_id}")
        print(Fore.CYAN + f"{Style.BRIGHT}Name: {Style.NORMAL}{student_data['name']}")
        print(Fore.GREEN + f"{Style.BRIGHT}Age: {Style.NORMAL}{student_data['age']}")
        
        print(Fore.MAGENTA + f"{Style.BRIGHT}Subjects:{Style.NORMAL}")
        for subject in student_data['subjects']:
            print(Fore.WHITE + f"- {subject}")
        
        print(Fore.RED + "=" * 50 + "\n")