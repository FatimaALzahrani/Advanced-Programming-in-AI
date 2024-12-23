![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=21&text=Exercise%201:%20Print%20Values%20and%20Define%20Pi&fontSize=45&animation=twinkling)

### Description:

In this exercise, I:

1. Print the values of `x`, `y`, and `z`.
2. Define a variable to store the value of **π (Pi)**.
3. Discuss defining constant in python.

### Output

![Output](https://github.com/user-attachments/assets/6e11bae8-3e0d-4ffd-a57a-dcf252285e2c)

### Code Implementation:

#### Solution 1: Print the values of `x`, `y`, and `z`.

        x = 12.2
        y = 14
        z = "65"

        # Print the values
        print("x =", x)
        print("y =", y)
        print("z =", z)

#### Solution 2: Define a variable to store the value of **π (Pi)**.

        PI = math.pi
        PI_approx = 3.14  # Approximate value of Pi without using math library

        print("The value of Pi using math module is:", PI)
        print("Approximate value of Pi is:", PI_approx)

#### Solution 3: Defining Constants in Python

        # Constants are typically defined by convention in uppercase
        PI = 3.14159  # A constant value for Pi

        print("Value of Pi as a constant:", PI)

### Code Explanation

#### 1. **Importing the `colorama` Library**:

        from colorama import Fore, Back, Style, init

##### The `colorama` library is used to add color to the terminal text output.

**Fore**: Controls the text color (foreground).
**Back**: Controls the background color.
**Style**: Controls the text style, such as brightness or normal.
**init(autoreset=True)**: Initializes colorama with the autoreset option, which automatically resets the color after each print statement to avoid affecting subsequent prints.

#### 2. The `print_styled` Function:

        def print_styled(text, fg_color, bg_color=Back.RESET, style=Style.NORMAL, width=100):
            print(bg_color + fg_color + style + text.center(width))

##### This function prints text with customizable colors and style.

**text**: The text to be printed.
**fg_color**: Foreground color of the text.
**bg_color**: Background color (default is no background).
**style**: Text style, such as bold or normal.
**width**: Defines the width of the printed text, and the text is centered within that width.

#### 3. Solution 1: Printing the values of `x`, `y`, and `z`:

        def Solution1():
            title = "🐍 Exercise (1) 🐍"
            print_styled(title, Fore.YELLOW, Back.BLUE, Style.BRIGHT)
            # ...

This function prints a styled title, then defines and prints the values of `x`, `y`, and `z`.

`x` is updated from 12.2 to 100 before printing.

The values are printed using the `print_styled` function, with different colors for each variable.

#### 4. Solution 2: Defining the value of π (Pi):

        def Solution2():
            import math
            PI = math.pi  # Precise value of Pi using math library
            PI_approx = 3.14  # Approximate value of Pi without math library
            # ...

This function demonstrates defining **π (Pi)** using the `math` library for the precise value (`math.pi`) and provides an approximate value (`3.14`) without using any library.

The values are printed using the `print_styled` function.

#### 5. Solution 3: Defining Constants in Python:

        def Solution3():
            from dataclasses import dataclass
            @dataclass(frozen=True)
            class Constants:
                PI: float = 3.14159
            # ...

`dataclass(frozen=True)` is used to simulate constants in Python by making the class immutable.

`PI` is defined as a constant in the class Constants with a frozen state to prevent modification.

This solution also explains how Python handles constants and suggests using conventions like uppercase names or advanced techniques like `dataclasses` for immutability.
