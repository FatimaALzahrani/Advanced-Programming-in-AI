#  Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look or lines that start with “From”,
"""
 then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

 Sample Line:
 From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

 Sample Execution:
 python dow.py
 Enter a file name: mbox-short.txt
 {Fri: 20, Thu: 6, Sat: 1}
"""

from colorama import Fore,init

init(autoreset=True)

def days(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()
                dictionary[email[2]] = 1 if email[2] not in dictionary else dictionary[email[2]]+1
        return dictionary

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    dictionary = days(file_name)
    print(f"{Fore.GREEN}{dictionary}")
