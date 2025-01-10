"""
Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:

    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5
    Enterafilename: mbox.txt
    zqian@umich.edu 195
"""

import re
from colorama import Fore,init

init(autoreset=True)


def emails(file):
    dictionary={}
    with open('Lecture9/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()
                dictionary[email[1]] = 1 if email[1] not in dictionary else dictionary[email[1]]+1
        return dictionary
    
def list_tuple(dictionary):
    list_emails = []
    for d in dictionary:
        list_emails.append((d,dictionary[d]))
    list_emails.sort(reverse=True, key=lambda x: x[1])
    return list_emails

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    dictionary = emails(file_name)
    email_info = list_tuple(dictionary)
    print(f"{Fore.MAGENTA}{email_info[0][0]} {Fore.GREEN}{email_info[0][1]}")
