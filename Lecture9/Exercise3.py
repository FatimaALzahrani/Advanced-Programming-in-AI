"""
Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z.
Your program should not count spaces, digits, punctuation, or any thing other than the letters a-z.
Find text samples from several different languages and see how letter frequency varies between languages.
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies
"""

from colorama import Fore,init

init(autoreset=True)

# def letters_frequency(file):
#     letter_frequency={}
#     with open('Lecture8/'+file,'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             if line.startswith('From '):
#                 words = line.split()
#                 # for w in 
#                 letter_frequency[words[1]] = 1 if letter_frequency[1] not in letter_frequency else letter_frequency[words[1]]+1
#         return letter_frequency
    
def letter_freq(file_name):
    letter_counts = {}

    with open('Lecture8/'+file_name, 'r') as file:
        for line in file:
            line = line.lower()
            for char in line:
                if 'a' <= char <= 'z':
                    letter_counts[char] = letter_counts.get(char, 0) + 1

    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_letter_counts:
        print(f"{Fore.GREEN}{letter}: {Fore.MAGENTA}{count}")

if __name__ == '__main__':
    file_name = input(f"{Fore.BLUE}Enter File name : {Fore.YELLOW}")
    letter_freq(file_name)
    # print(f"{Fore.GREEN}{dictionary}")
