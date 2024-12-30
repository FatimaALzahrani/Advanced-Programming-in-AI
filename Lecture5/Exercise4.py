# Split a string into words and count their occurrences.
from colorama import Fore, Style

def words_count(string):
    words = string.split(" ")
    print(f"{Fore.YELLOW}Word occurrences:")
    for i in range(len(words)):
        word = words[i]
        if word not in words[:i]: 
            count = 0
            for w in words:
                if w == word:
                    count += 1
            print(f"{Fore.MAGENTA}{word}: {Fore.GREEN}{count}") 

if __name__ == '__main__':
    text = input(f"{Fore.BLUE}Enter an text : {Fore.LIGHTGREEN_EX}")
    words_count(text)