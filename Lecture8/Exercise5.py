# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
"""
python schoolcount.py
Enter a file name: mbox-short.txt
{media.berkeley.edu: 4, uct.ac.za: 6, umich.edu: 7,
gmail.com: 1, caret.cam.ac.uk: 1, iupui.edu: 8}
"""

from colorama import Fore,init

init(autoreset=True)


def domains(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()[1].split('@')
                dictionary[email[1]] = 1 if email[1] not in dictionary else dictionary[email[1]]+1
        return dictionary
    
if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    dictionary = domains(file_name)
    print(f"{Fore.MAGENTA}{dictionary}")
