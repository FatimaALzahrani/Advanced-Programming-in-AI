from colorama import Fore, Back, Style, init

init(autoreset=True)

def print_styled(text, fg_color, bg_color=Back.RESET, style=Style.NORMAL, width=100):
    print(bg_color + fg_color + style + text.center(width))

def Solution1():
    title = "🐍 Exercise (1) 🐍"
    print_styled(title, Fore.YELLOW, Back.BLUE, Style.BRIGHT)

    print("=" * 100)

    Q1 = "📌 1. Print the values of x, y, and z."
    print_styled(Q1, Fore.MAGENTA, Back.WHITE, Style.BRIGHT)

    print("=" * 100)

    # تعريف المتغيرات
    x = 12.2  # تم تعيين القيمة الأولية
    y = 14
    z = "65"

    # تم تحديث قيمة x إلى 100
    x = 100  # قيمة جديدة لـ x

    # طباعة القيم
    print_styled(f"x = {x}", Fore.CYAN)
    print_styled(f"y = {y}", Fore.GREEN)
    print_styled(f"z = {z}", Fore.MAGENTA)

    print("\n" + "🐍" * 50 + "\n")

def Solution2():
    print("=" * 100)
    Q2 = "📌 2. Define a variable to store the value of π (pi)."
    print_styled(Q2, Fore.MAGENTA, Back.WHITE, Style.BRIGHT)

    print("=" * 100)

    import math
    PI = math.pi  # قيمة π الدقيقة
    PI2 = 3.14  # قيمة تقريبية للـ π

    # طباعة القيم
    print_styled(f"π using math module: {PI}", Fore.CYAN)
    print_styled(f"Approximate value of π: {PI2}", Fore.GREEN)

    print("\n" + "🐍" * 50 + "\n")

def Solution3():
    print("=" * 100)
    Q3 = "📌 3. Discuss defining constants in Python."
    print_styled(Q3, Fore.MAGENTA, Back.WHITE, Style.BRIGHT)

    print("=" * 100)

    from dataclasses import dataclass

    # استخدام dataclass لمحاكاة الثوابت
    @dataclass(frozen=True)
    class Constants:
        PI: float = 3.14159

    constants = Constants()

    # طباعة قيمة الثابت
    print_styled(f"PI constant value: {constants.PI}\n", Fore.CYAN)
    print_styled("Defining constants in Python:", Fore.YELLOW, Style.BRIGHT)
    
    # شرح تعريف الثوابت في بايثون
    Answer3 = (
        "Python does not have built-in support for constants like other programming languages.\n"
        "By convention, we use uppercase variable names to indicate that a value is constant,\n"
        "but this does not enforce immutability.\n"
        "To ensure a value cannot be changed, we can use advanced methods like 'dataclasses' with 'frozen=True' or libraries."
    )
    print_styled(Answer3, Fore.LIGHTCYAN_EX, Style.DIM)

    print("\n" + "🐍" * 50 + "\n")

if __name__ == '__main__':
    Solution1()
    Solution2()
    Solution3()