# Write a program to count the occurrences of a character in a string.
from colorama import Fore,init
init(autoreset=True)

# Using count build-in function
def count_character_occurrences(string, char):
    count = string.count(char)
    return count

# Using nested loop
def count_each_character(string):
    for i in range(len(string)):
        if string[i] not in string[:i]:
            count = 0
            for j in range(len(string)):
                if string[i] == string[j]:
                    count += 1
            print(f"{Fore.YELLOW}'{string[i]}'{Fore.GREEN}: {count}")

# Using for loop
def count_characters(s,c):
    total = 0
    for ch in s:
        if(ch==c):
            total+=1
    return total

if __name__ == '__main__':
    string = input(f"{Fore.BLUE}Enter a string: {Fore.LIGHTGREEN_EX}")
    char = input(f"{Fore.YELLOW}Enter the character to count: {Fore.LIGHTGREEN_EX}")

    if len(char) != 1:
        print(f"{Fore.RED}Please enter only a single character.")
    else:
        occurrences = count_character_occurrences(string, char)
        print(f"{Fore.MAGENTA}The character {Fore.YELLOW}'{char}'{Fore.MAGENTA} appears {Fore.GREEN}{occurrences}{Fore.MAGENTA} times in the string.")

    print(f"{Fore.YELLOW}Character counts:")
    count_each_character(string)
