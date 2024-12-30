# Python Exercises - Loops, Functions, and Exception Handling

![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=23&text=Exercises%20of%20Chapter%204&fontSize=61&animation=twinkling)

This folder contains a series of Python exercises that involve loops, functions, and exception handling. The exercises cover various concepts such as calculating factorials, printing odd numbers, and handling user inputs gracefully.

## Table of Contents

1. [Odd Numbers Loop (for and while)](#odd-numbers-loop-for-and-while)
2. [Factorial Calculation using Loop](#factorial-calculation-using-loop)
3. [Factorial Calculation using Loop with error handleing](#factorial-calculation-using-loop-error)
4. [Exercise Solutions](#exercise-solutions)
   - [Exercise 4](#exercise-4-what-is-the-purpose-of-the-def-keyword-in-python)
   - [Exercise 5](#exercise-5-what-will-the-program-print-out)
   - [Exercise 6](#exercise-6-time-and-a-half-pay-computation)
   - [Exercise 7](#exercise-7-grade-computation)
5. [How to Run](#how-to-run)
6. [License](#license)

## Odd Numbers Loop (for and while)

This exercise demonstrates how to print all `odd numbers` between 1 and 10 using both `for` and `while` loops.

**Code Snippet**:

```python
# Using for loop
for num in range(1, 11):
    if num % 2 != 0:
        print(num)

# Using while loop
num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image.png)

## Factorial Calculation using Loop

This program calculates the `factorial` of a number using both `for` and `while` loops.

**Code Snippet**:

```python
    # Using for loop
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)

    # Using while loop
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(factorial)
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image-1.png)

## Factorial Calculation using Loop with error handling

This program calculates the `factorial` of a number using both `for` and `while` loops. It also includes `exception handling` for invalid inputs.

**Code Snippet**:

```python
def calculate_factorial():
    try:
        num = int(input(f"Enter a non-negative integer: "))
        if num < 0:
            print(f"Factorial is not defined for negative numbers.")

        # Using for loop
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"{factorial}")

        # Using while loop
        factorial = 1
        i = 1
        while i <= num:
            factorial *= i
            i += 1
        print(f"Factorial of {num} using while loop is: {factorial}")
    except:
        print(f"Invalid input")

calculate_factorial()
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image-2.png)

## **What is the purpose of the `def` keyword in Python?**

### **Exercise 4:**

What is the purpose of the “def” keyword in Python?

**Options:**  
a) It is slang that means “the following code is really cool”  
b) It indicates the start of a function  
c) It indicates that the following indented section of code is to be stored for later  
d) b and c are both true  
e) None of the above

### **Answer:**

**`d) b and c are both true`**

### **Explanation:**

The `def` keyword in Python is used to define a **function**. Functions are reusable blocks of code designed to perform specific tasks.

- **Option b:** Correct, because `def` marks the start of a function.
- **Option c:** Correct, because the indented block of code after `def` is stored for later execution when the function is called.
- **Option d:** Correct, as both b and c are true.
- **Option a:** Incorrect, this is a humorous option.
- **Option e:** Incorrect, because both b and c are valid.

### **Example:**

```python
# Define a function using the 'def' keyword
def greet(name):
    """
    This function greets the person whose name is passed as an argument.
    """
    print(f"Hello, {name}! Welcome to Python.")

# Call the function
greet("Fatimah")  # Output: Hello, Fatimah! Welcome to Python.
greet("Mohammed") # Output: Hello, Mohammed! Welcome to Python.
```

## What will the program print out?

```python
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()
```

**Answer**:
`d) ABC Zap ABC`

The program calls jane() which prints "ABC", then fred() which prints "Zap", and then jane() again prints "ABC".

## Time-and-a-Half Pay Computation

Rewrite your pay computation with time-and-a-half for overtime and
create a `function` called `computepay` which takes two `parameters (hours and rate)`

**Code Snippet**:

```python
def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        if hours > 40:
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * (rate * 1.5)
            total_pay = (40 * rate) + overtime_pay
        else:
            total_pay = hours * rate

        return f"Total Pay: {total_pay}"
    except:
        return f"Invalid input. Please enter numeric values."

# Input
hours = input(f"Enter Hours: ")
rate = input(f"Enter Rate: ")
print(computepay(hours, rate))
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise6.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image-4.png)

## Grade Computation

Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as a
string.

**Code Snippet**:

```python
def computegrade(score):
    try:
        score = float(score)
        if score > 1.0 or score < 0.0:
            return f"Bad score"
        elif score >= 0.9:
            return f"A"
        elif score >= 0.8:
            return f"B"
        elif score >= 0.7:
            return f"C"
        elif score >= 0.6:
            return f"D"
        else:
            return f"F"
    except:
        return f"Bad score"

# Input and Testing
while True:
    user_input = input(f"Enter score (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    print(computegrade(user_input))
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise7.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image-3.png)
