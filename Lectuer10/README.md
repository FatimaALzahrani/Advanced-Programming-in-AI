![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=16&text=Exercises%20of%20Chapter%2010&fontSize=61&animation=twinkling)

Here solutions to the Exercises from Chapter 10 - Sets

<!-- To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/practical.ipynb) -->

## Table of Contents

1.  [Create a set of numbers and add a new number to it.](#ex1_1)
2.  [Write a program to find the union and intersection of two sets.](#ex1_2)
3.  [Remove all duplicates from a list using a set.](##ex1_3)
4.  [Create two sets and check if one is a subset of the other.](##ex1_4)

## 1. Create a set of numbers and add a new number to it.<a name="ex1_1"></a>

**Code Snippet**:

```python
phone_numbers = {1234567890, 9876543210, 1122334455}
new_phone = int(input("Enter a new phone number to add: "))
print(f"Phone numbers: {phone_numbers}")
phone_numbers.add(new_phone)
print(f"Updated phone numbers: {phone_numbers}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Screenshots/image.png)

<hr/>

## 2. Write a program to find the union and intersection of two sets.<a name="ex1_2"></a>

**Code Snippet**:

```python
programming_course = {"Ahmed", "Fatimah", "Nada", "Noura"}
design_course = {"Fatimah", "Mohammed", "Noura", "Shaekah"}

# • Union: Combine elements from both sets.
union_result = programming_course | design_course
# • Intersection: Common elements between sets.
intersection_result = programming_course & design_course

print(f"Students in programming course : {programming_course}")
print(f"Students in design course : {design_course}")
print(f"Students in at least one course 'Union' : {union_result}")
print(f"Students in both courses 'Intersection' : {intersection_result}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Screenshots/image-1.png)

<hr/>

## 3. Remove all duplicates from a list using a set.<a name="ex1_3"></a>

**Code Snippet**:

```python
purchases = ["Apple", "Orange", "Apple", "Banana", "Orange", "Grapes"]
unique_purchases = list(set(purchases))
print(f"Original purchases list: {purchases}")
print(f"Unique purchases: {unique_purchases}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Screenshots/image-2.png)

<hr/>

## 4. Create two sets and check if one is a subset of the other<a name="ex1_4"></a>

**Code Snippet**:

```python
# Create two sets
set_a = {"Laptop", "Notebook", "Pen"}
set_b = {"Laptop", "Notebook", "Pen", "Tablet", "Phone"}

print(f"Set A : {set_a}")
print(f"Set B : {set_b}")

# Check if one set is a subset of the other
if set_a.issubset(set_b):
    print("Set A is a subset of Set B.")
else:
    print("Set A is NOT a subset of Set B.")

if set_b.issubset(set_a):
    print("Set B is a subset of Set A.")
else:
    print("Set B is NOT a subset of Set A.")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture10/Screenshots/image-3.png)
