#  Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
from colorama import Fore,init

init(autoreset=True)

def  extract_float(s):
    index = s.find(':')+1
    return float(s[index:].strip())

# s = 'X-DSPAM-Confidence: 0.8475'
# f = extract_float(s)
s = input(f"{Fore.BLUE}Enter an string with : and floating point number : {Fore.YELLOW}")
f = extract_float(s)
print(f"{Fore.GREEN}The portion of the string {Fore.YELLOW}{s}{Fore.GREEN} after the colon character as float is {Fore.MAGENTA}{f}")