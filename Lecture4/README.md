![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=23&text=Exercises%20of%20Chapter%204&fontSize=61&animation=twinkling)

Here solutions to the Exercises from Chapter 4 - Iteration

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/practical.ipynb)

## Table of Contents

1. [Odd Numbers Loop (for and while)](#odd-numbers-loop-for-and-while)
2. [Factorial Calculation using Loop](#factorial-calculation-using-loop)
3. [Factorial Calculation using Loop with error handleing](#factorial-calculation-using-loop-error)
4. Do the exercises on pages 76 and 77 of the book
   - [ Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.](#repeatedly)
   - [Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.](#list_num)

## Odd Numbers Loop (for and while) <a name="odd-numbers-loop-for-and-while"></a>

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

## Factorial Calculation using Loop <a name="factorial-calculation-using-loop"></a>

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

## Factorial Calculation using Loop with error handling <a name="factorial-calculation-using-loop-error"></a>

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

## Write a program which repeatedly reads integers until the user enters “done”. <a name="repeatedly"></a>

Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.

**Code Snippet**:

```python
count = 0
total = 0
print("Enter integers one by one (type 'done' to finish.)")
while True:
    num = input()
    if num.lower()=="done":
        average = total/count
        print(f"Total: {total}, Count: {count}, Average: {average}")
        break
    try:
        total+=int(num)
        count+=1
    except:
        print("Something went wrong, please enter an integer!")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image-4.png)

## prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers <a name="list_num"></a>

Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

**Code Snippet**:

```python
max_num = None
min_num = None

while True:
    num = input("Enter number: ")

    if num.lower() == "done":
        if max_num is not None and min_num is not None:
            print(f"Maximum: {max_num} And Minimum: {min_num}")
        else:
            print(f"No valid numbers were entered.")
        break

    try:
        num = int(num)
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num

    except:
        print("Invalid data. Please enter a valid number.")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture4/Screenshots/image-5.png)
