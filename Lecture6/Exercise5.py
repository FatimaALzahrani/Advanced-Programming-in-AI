#  5. Do the exercises on pages 89 and 90 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024

"""
Exercise 1: Write a program to read through a file and print the contents of the
 file (line by line) all in upper case. Executing the program will look as follows:
"""

#  python shout.py
#  Enter a file name: mbox-short.txt
#  FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
#  RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#  RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#  BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#  SAT, 05 JAN 2008 09:14:16-0500

#  You can download the file from www.py4e.com/code3/mbox-short.txt

from colorama import Fore,init

init(autoreset=True)

file_name=input(f"{Fore.BLUE}Enter a file name: ")

with open('Lecture6/'+file_name) as file:
    lines=file.readlines()#[:5]
    for line in lines:
        print(f"{Fore.BLUE}{line.upper()}",end='')