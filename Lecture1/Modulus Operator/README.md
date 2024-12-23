![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=22&text=Modulus%20Operator&fontSize=61&animation=twinkling)

Read and summarise (2.8 Modulus operator ) p 24 from the Python for Everybody book

The **modulus operator** works on integers and returns the remainder when the first operand is divided by the second. In Python, the modulus operator is represented by the percent sign (`%`). The syntax is similar to other operators in Python.

### Key Points:

1. **Basic Usage**:

   - `7 // 3` yields the quotient (`2`).
   - `7 % 3` yields the remainder (`1`).

2. **Applications**:
   - **Divisibility Check**:
     - If `x % y == 0`, then `x` is divisible by `y` without a remainder. [Example](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture1/Modulus%20Operator/Divisibility%20Check.py)
   - **Digit Extraction**:
     - `x % 10` extracts the right-most digit of `x` in base 10.
     - `x % 100` extracts the last two digits of `x`.
     - [Example](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture1/Modulus%20Operator/Digit%20Extraction.py)

### Example Code:

        quotient = 7 // 3
        print(quotient)  # Output: 2

        remainder = 7 % 3
        print(remainder)  # Output: 1
