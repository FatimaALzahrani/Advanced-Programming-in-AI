# Write a program to count the frequency of words in a string using a dictionary.

from colorama import Fore,init

init(autoreset=True)

def count_words(text):
    dictionary={}
    words=text.split(' ')
    for word in words:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
    return dictionary

if __name__ == '__main__':
    text = input(f"{Fore.BLUE}Enter an string : {Fore.YELLOW}")
    frequency = count_words(text)
    for word in frequency:
        print(f"{Fore.GREEN}{word} : {Fore.MAGENTA}{frequency[word]}")