from colorama import Fore, Style, init

def compute_pay_with_error_handling():
    """
    Prompts the user for hours and rate, computes pay, and handles invalid inputs.
    """
    try:
        hours = float(input(Fore.MAGENTA+"Enter Hours: "))
        rate = float(input(Fore.MAGENTA+"Enter Rate: "))
        if hours > 40:
            overtime_hours = hours - 40
            pay = (40 * rate) + (overtime_hours * rate * 1.5)
        else:
            pay = hours * rate
        print(Fore.GREEN+f"Pay: {pay:.2f}")
    except ValueError:
        print(Fore.RED+"Error, please enter numeric input.")


# use the function
if __name__ == "__main__":
    compute_pay_with_error_handling()
