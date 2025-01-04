#  6. Do the exercises on pages 105,106 and 107 of the book
"""
Exercise 5: Minimalist Email Client.
MBOX(mail box) is a popular file format to store and share a collection of emails.
This was used by early email servers and desktop apps. 
Without getting into too many details, MBOX is a text file, which stores emails consecutively. 
Emails are separated by a special line which starts with From (notice the space). 
Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. 
Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.
Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. 
We are interested in who sent the message, which is the second word on the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 You will parse the From line and print out the second word for each From line, 
then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:
python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
[...some output removed...]
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu

There were 27 lines in the file with From as the first word
"""
from colorama import Fore,init

init(autoreset=True)

file_name = input(f"{Fore.BLUE}Enter File: {Fore.YELLOW}")
num = 0

with open('Lecture7/'+file_name,'r') as file:
    lines_list = file.readlines()
    for line in lines_list:
        if line.strip().startswith('From:'):
            print(f"{Fore.LIGHTMAGENTA_EX}{line.split(" ")[1]}",end='')
            num+=1
    print(f"{Fore.GREEN}There were {Fore.MAGENTA}{num} {Fore.GREEN}lines in the file with From as the first word")