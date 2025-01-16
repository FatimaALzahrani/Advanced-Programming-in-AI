#  Exercise 1: Download a copy of the file
"""
 www.py4e.com/code3/words.txt
 Write a program that reads the words in words.txt and stores them as keys in
 a dictionary. It doesn’t matter what the values are. Then you can use the in
 operator as a fast way to check whether a string is in the dictionary.
"""

import re
from colorama import Fore,init

init(autoreset=True)


def read_words(file):
    dic = {}
    with open('Lecture8/'+file,'r') as file:
        # lines = file.read().split('\n')
        words = re.split(r'[\n\s]+', file.read())
        # words = [line.split() for line in lines]
        for word in words:
            dic[word]=''
    return dic

def check_string(dictionary,word):
    return word in dictionary

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    word = input(f"{Fore.BLUE}Enter string : {Fore.YELLOW}")
    dictionary = read_words(file_name)
    in_dic = check_string(dictionary,word)
    if(in_dic):
        print(f"{Fore.LIGHTYELLOW_EX}{word}{Fore.GREEN} is {Fore.MAGENTA}in {Fore.GREEN}the dictionary of file {Fore.LIGHTYELLOW_EX}{file_name}!")
    else:
        print(f"{Fore.LIGHTYELLOW_EX}{word} {Fore.RED}is not in{Fore.GREEN} the dictionary of file {Fore.LIGHTYELLOW_EX}{file_name}!")
