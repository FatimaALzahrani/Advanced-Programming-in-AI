from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print("\nThis script demonstrates Python string methods with examples and colorful outputs.\n")

# 1. Using strip() to clean up whitespace
dirty_string = "   Hello, World!   "
clean_string = dirty_string.strip()
print(f"{Fore.RED}Before strip:{Style.RESET_ALL} '{dirty_string}'")
print(f"{Fore.GREEN}After strip:{Style.RESET_ALL} '{clean_string}'\n")

# 2. Using replace() to replace substrings
text = "I love Java programming language"
new_text = text.replace("Java", "Python")
print(f"{Fore.BLUE}Before replace:{Style.RESET_ALL} '{text}'")
print(f"{Fore.YELLOW}After replace:{Style.RESET_ALL} '{new_text}'\n")

# 3. Using find() to locate a substring
sentence = "The quick brown fox jumps over the lazy dog."
position = sentence.find("fox")
print(f"{Fore.LIGHTGREEN_EX}Text:{Style.RESET_ALL} {sentence}")
print(f"{Fore.CYAN}The word 'fox' is found at index:{Style.RESET_ALL} {position}\n")

# 4. strip & replace
dirty_text = "   Fatimah Alzahrani   "
clean_replaced_text = dirty_text.strip().replace("Alzahrani", "Mohammed")
print(f"{Fore.LIGHTRED_EX}Result before cleaning and replacing:{Style.RESET_ALL} '{dirty_text}'")
print(f"{Fore.MAGENTA}Result after cleaning and replacing:{Style.RESET_ALL} '{clean_replaced_text}'\n")

print(f"{Style.BRIGHT}{Fore.WHITE}String methods are essential for text processing. Combine them for powerful results!{Style.RESET_ALL}")
