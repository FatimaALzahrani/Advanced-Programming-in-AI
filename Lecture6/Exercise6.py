#  5. Do the exercises on pages 89 and 90 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024

"""
Exercise 2: Write a program to prompt for a file name, and then read through
 the file and look for lines of the form:

  X-DSPAM-Confidence: 0.8475

 When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
 the line to extract the floating-point number on the line. Count these lines and
 then compute the total of the spam confidence values from these lines. When you
 reach the end of the file, print out the average spam confidence.
"""

#  Enter the file name: mbox.txt
#  Average spam confidence: 0.894128046745
#  Enter the file name: mbox-short.txt
#  Average spam confidence: 0.750718518519

#  Test your file on the mbox.txt and mbox-short.txt files.

from colorama import Fore,init

init(autoreset=True)

file_name=input(f"{Fore.BLUE}Enter a file name: ")
total=0
count=0

with open('Lecture6/'+file_name,'r') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if(line.startswith('X-DSPAM-Confidence:')):
            index=line.find(':')+1
            f=float(line[index:].strip())
            total+=f
            count+=1
    avg=total/count
    print(f"{Fore.GREEN}Average spam confidence: {Fore.MAGENTA}{avg}")