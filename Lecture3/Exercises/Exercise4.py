from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def compute_pay(hours, rate):
    """
    Computes the pay for an employee based on hours worked and hourly rate.
    Overtime (above 40 hours) is paid at 1.5 times the regular rate.
    
    Parameters:
    hours (float): Number of hours worked.
    rate (float): Hourly rate of pay.
    
    Returns:
    float: Total pay.
    """
    if hours > 40:
        overtime_hours = hours - 40
        return (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        return hours * rate


# use the function
if __name__ == "__main__":
    try:
        hours = float(input(Fore.BLUE+"Enter Hours: "))
        rate = float(input(Fore.BLUE+"Enter Rate: "))
        pay = compute_pay(hours, rate)
        print(Fore.GREEN+f"Pay: {pay:.2f}")
    except:
        print(Fore.RED+"Error, please enter numeric input.")
