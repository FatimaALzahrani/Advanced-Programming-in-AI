"""
This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string and then split ting that string into parts using the colon character. 
Once you have accumulated the counts for each hour,print out the counts,one perline, sorted by hour as shown below

    python timeofday.py
    Enter a file name: mbox-short.txt
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1
"""

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

from colorama import Fore,init

init(autoreset=True)

def hours(file):
    dictionary={}
    with open('Lecture9/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()[5].split(':')
                dictionary[email[0]] = 1 if email[0] not in dictionary else dictionary[email[0]]+1
        return dictionary

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    dictionary = hours(file_name)
    list_tuple = sorted(dictionary.items(), key=lambda x: x[0], reverse=False)
    for hour,count in list_tuple:
        print(f"{Fore.GREEN}{hour} {Fore.MAGENTA}{count}")
