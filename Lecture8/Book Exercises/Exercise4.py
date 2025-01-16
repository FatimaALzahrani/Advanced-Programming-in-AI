# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
"""
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
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
    
def maximum(emails):
    # return max(dic)
    largest = None
    em = None
    for email in emails:
        if largest == None or emails[email]>largest:
            largest = emails[email]
            em = email
    return largest,em

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    dictionary = emails(file_name)
    maximum_num,email = maximum(dictionary)
    print(f"{Fore.MAGENTA}{email} {Fore.GREEN}{maximum_num}")
