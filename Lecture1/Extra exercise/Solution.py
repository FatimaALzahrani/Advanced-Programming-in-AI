from colorama import Fore, Style, init

init()

hours = float(input(Fore.CYAN + "⏰ Enter Hours: " + Style.RESET_ALL))  
rate = float(input(Fore.CYAN + "💵 Enter Rate: " + Style.RESET_ALL)) 

pay = hours * rate

print(Fore.GREEN + f"💰 Pay: {pay:.2f}" + Style.RESET_ALL)  