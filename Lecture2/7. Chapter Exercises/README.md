![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=12&text=Chapter%20Exercises%20&animation=fadeIn)

Here solutions to the Exercises from Chapter 2 - Conditional Expression

## Table of Contents

1. [Overtime Pay Calculation](#overtime-pay-calculation)
2. [Overtime Pay Calculation with Error Handling](#overtime-pay-calculation-with-error-handling)
3. [Grade Calculation Based on Score](#grade-calculation-based-on-score)

<hr>

###

### 1. Overtime Pay Calculation <a name="overtime-pay-calculation"></a>

**Functionality**:  
Calculate the pay for an employee, with 1.5 times the hourly rate for any hours worked above 40.

**Code Snippet**:

```python
def compute_pay(hours, rate):
    if hours > 40:
        overtime = (hours - 40) * (rate * 1.5)
        return (40 * rate) + overtime
    else:
        return hours * rate
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Screenshots/image-4.png)

### 2. Overtime Pay Calculation with Error Handling <a name="pay-calculation-with-error-handling"></a>

**Functionality**:  
Handle non-numeric input gracefully by printing an error message.

**Code Snippet**:

```python
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print("Pay:", compute_pay(hours, rate))
except ValueError:
    print("Error, please enter numeric input")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Screenshots/image-5.png)
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Screenshots/image-6.png)

### 3. Grade Calculation Based on Score <a name="grade_calculation"></a>

**Functionality**:  
Prompt the user for a score between 0.0 and 1.0 and assign a grade based on the following table:

**Code Snippet**:

```python
def compute_grade(score):
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

try:
    score = float(input("Enter Score: "))
    if 0 <= score <= 1:
        print("Grade:", compute_grade(score))
    else:
        print("Bad Score")
except ValueError:
    print("Bad Score")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Screenshots/https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture2/7. Chapter Exercises/Screenshots/image-7.png)
