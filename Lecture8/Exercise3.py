# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
"""
Enter file name: mbox-short.txt
{gopal.ramasammycook@gmail.com: 1, louis@media.berkeley.edu: 3,
cwen@iupui.edu: 5, antranig@caret.cam.ac.uk: 1,
rjlowe@iupui.edu : 2, gsilver@umich.edu: 3,
david.horwitz@uct.ac.za: 4, wagnermr@iupui.edu: 1,
zqian@umich.edu: 4, stephen.marquard@uct.ac.za: 2,
ray@media.berkeley.edu: 1}
"""

from colorama import Fore,init

init(autoreset=True)

def emails(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()
                dictionary[email[1]] = 1 if email[1] not in dictionary else dictionary[email[1]]+1
        return dictionary

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    dictionary = emails(file_name)
    print(f"{Fore.GREEN}{dictionary}")
