# Write a program to find the union and intersection of two sets.
from colorama import Fore, Style

if __name__ == '__main__':
    programming_course = {"Ahmed", "Fatimah", "Nada", "Noura"}
    design_course = {"Fatimah", "Mohammed", "Noura", "Shaekah"}

    # • Union: Combine elements from both sets.
    union_result = programming_course | design_course
    # • Intersection: Common elements between sets.
    intersection_result = programming_course & design_course

    print(f"{Fore.BLUE}Students in programming course : {Fore.LIGHTYELLOW_EX}{programming_course}")
    print(f"{Fore.BLUE}Students in design course : {Fore.LIGHTYELLOW_EX}{design_course}")
    print(f"{Fore.GREEN}Students in at least one course 'Union' : {Fore.MAGENTA}{union_result}")
    print(f"{Fore.GREEN}Students in both courses 'Intersection' : {Fore.MAGENTA}{intersection_result}")
