![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=12&text=Chapter%20Exercises%20&animation=fadeIn)

Here solutions to the Exercises from Chapter 3 - Functions

## Table of Contents

1. [Multiplying Two Numbers](#multiplying-two-numbers)
2. [Checking If a Number is Even](#checking-if-a-number-is-even)
3. [Generating a Random Number Between Two Values](#generating-a-random-number-between-two-values)
4. Book Exercise Solutions
   - [Exercise 4](#exercise-4-what-is-the-purpose-of-the-def-keyword-in-python)
   - [Exercise 5](#exercise-5-what-will-the-program-print-out)
   - [Exercise 6](#exercise-6-time-and-a-half-pay-computation)
   - [Exercise 7](#exercise-7-grade-computation)
   <hr>

###

### 1. Multiplying Two Numbers <a name="multiplying-two-numbers"></a>

**Functionality**:  
This function takes two arguments and returns their `product`.

**Code Snippet**:

```python
def multiply(number1, number2):
    return number1 * number2
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Screenshots/image-3.png)

### 2. Checking If a Number is Even <a name="checking_is_even"></a>

**Functionality**:  
This function checks if a given number is `even` or odd.

**Code Snippet**:

```python
def is_even(number):
    return number % 2 == 0
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Screenshots/image-1.png)
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Screenshots/image-2.png)

### 3. Generating a Random Number Between Two Given Values <a name="generating_random_number"></a>

**Functionality**:  
This function generates a `random` number between two specified numbers using Python's random module.

**Code Snippet**:

```python
import random

def random_number_between(num1, num2):
    return random.randint(num1, num2)
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Screenshots/image.png)

## **What is the purpose of the `def` keyword in Python?** <a name="exercise-4-what-is-the-purpose-of-the-def-keyword-in-python"></a>

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

## What will the program print out? <a name="exercise-5-what-will-the-program-print-out"></a>

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

## Time-and-a-Half Pay Computation <a name="exercise-6-time-and-a-half-pay-computation"></a>

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Exercise6.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Screenshots/image-pay.png)

## Grade Computation <a name="exercise-7-grade-computation"></a>

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Exercise7.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture3/Exercises/Screenshots/image-grade.png)
