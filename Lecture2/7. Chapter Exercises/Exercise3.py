from colorama import Fore , init, Style

init(autoreset=True)

def compute_grade(score):
    """
        Computes the grade based on the score.
        
        Parameters:
        score (float): A score between 0.0 and 1.0.
        
        Returns:
        str: The grade (A, B, C, D, F) or an error message for invalid scores.
    """
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

# use the function
if __name__ == '__main__':
    try:
        score = float(input(Fore.YELLOW+"Enter Score : "))
        if 0 <= score <= 1:
            grade = compute_grade(score)
            print(Fore.GREEN + f"Grade: {grade}")
        else:
            print(Fore.RED + "Bad Score")
    except:
        print(Fore.RED + "Bad Score")