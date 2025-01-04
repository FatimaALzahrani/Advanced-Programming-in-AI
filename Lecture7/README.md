![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=25&text=Chapter%20Exercises%20&animation=fadeIn)

Here solutions to the Exercises from Chapter 7 - Lists

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/practical.ipynb)

## Table of Contents

1. [Create a list of numbers and find the largest and smallest numbers.](#largest_smallest)
2. [Write a program to remove duplicates from a list.](#duplicates)
3. [Create a list of squares for numbers 1 through 10 using list comprehension.](#list_comprehension)
4. [Write a program to merge two lists without duplicates.](#merge)
5. [How to remove more than one element in a list (see p.95).](#remove_multy)
6. [Do the exercises on pages 105,106 and 107 of the book](#book)
   - [Exercise 4: Find all unique words in a file Shakespeare used over 20,000 words in his works. ](#unique_words)
   - [Exercise 5: Minimalist Email Client.](#Minimalist_Email)
   - [Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.](#maximum_minimum)

## 1. Create a list of numbers and find the largest and smallest numbers. <a name="largest_smallest"></a>

**Code Snippet**:
Sevrel way to do it

### using build in function sorted

```python
def with_sorted(list_num):
    sorted_list=sorted(list_num)

    largest = sorted_list[-1]
    smallest = sorted_list[0]

    print(f"Using Build-in function sorted : ")
    print(f"The Largest number is {largest}, and Smallest number is {smallest}")
```

### using build in function min & max

```python
def with_min_max(list_num):
    largest = max(list_num)
    smallest = min(list_num)

    print(f"Using Build-in functions min & max : ")
    print(f"The Largest number is {largest}, and Smallest number is {smallest}")
```

### using loop

```python
def with_loop(list_num):
    largest = list_num[0]
    smallest = list_num[0]
    for num in list_num:
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
    print(f"Using Loop : ")
    print(f"The Largest number is {largest}, and Smallest number is {smallest}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image.png)

## 2. Write a program to remove duplicates from a list. <a name="duplicates"></a>

**Code Snippet**:
Sevrel way to do it

### using set

```python
def with_set(list_num):
    list_uniq = list(set(list_num))
    print(f"List without duplicates using set : {list_uniq}")
```

### using loop with append

```python
def with_loop(list_num):
    list_uniq = []
    for num in list_num:
        if num not in list_uniq:
            list_uniq.append(num)

    print(f"List without duplicates using loop & append : {list_uniq}")
```

### using loop with remove

```python
def with_loop_remove(list_num):
    for num in list_num[:]:
        if list_num.count(num) > 1:
            list_num.remove(num)

    print(f"List without duplicates using loop & remove : {list_num}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-1.png)

## 3. Create a list of squares for numbers 1 through 10 using list comprehension. <a name="list_comprehension"></a>

**Code Snippet**:

```python
list_num = [n**2 for n in range(1,11)]

print(f"{list_num}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-2.png)

## 4. Write a program to merge two lists without duplicates.<a name="merge"></a>

**Code Snippet**:

### using loop and concationation

```python
def with_loop_concat(names_list1,names_list2):
    merged_names = names_list1+names_list2
    names = []
    for name in merged_names:
        if name not in names:
            names.append(name)
    print(f"Merged two lists without duplicates and using loop is {names}")
```

## using set and extend

```python
def with_set_extend(names1,names2):
    names1.extend(names2)
    names = list(set(names1))
    print(f"Merged two lists without duplicates  and using set is {names}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-3.png)

## 5. How to remove more than one element in a list (see p.95).<a name="remove_multy"></a>

**Code Snippet**:

```python
names = ['Ahmed', 'Mohammed', 'Abduallah', 'Fatimah']
print(f'Original list is : {names}')
del names[1:3]
print(f"List after del 1:3 : {names}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-4.png)

## Book Exercises <a name="book"></a>

### 6. Exercise 4: Find all unique words in a file Shakespeare used over 20,000 words in his works.<a name="unique_words"></a>

But how would you determine that?
How would you produce the list of all the words that Shakespeare used?
Would you download all his work, read it and track all unique words by hand?
Let’s use Python to achieve that instead.
List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result.
Write a program to open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in the list of unique words.
If the word is not in the list of unique words, add it to the list.
When the program completes, sort and print the list of unique words in alphabetical order.

    `Enter file: romeo.txt
    [Arise, But, It, Juliet, Who, already,
    and , breaks, east, envious, fair, grief,
    is, kill, light, moon, pale, sick , soft,
    sun , the, through, what, window,
    with, yonder]`

**Code Snippet**:

```python
file_name = input(f"Enter File: ")
unique_words = []

with open('Lecture7/'+file_name,'r') as file:
    lines_list = file.readlines()
    for line in lines_list:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    unique_words.sort()

print(f"{unique_words}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise6.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-5.png)

### 7. Exercise 5: Minimalist Email Client.<a name="Minimalist_Email"></a>

Exercise 5: Minimalist Email Client.
MBOX(mail box) is a popular file format to store and share a collection of emails.
This was used by early email servers and desktop apps.
Without getting into too many details, MBOX is a text file, which stores emails consecutively.
Emails are separated by a special line which starts with From (notice the space).
Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator.
Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.
Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function.
We are interested in who sent the message, which is the second word on the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:

    `python fromcount.py
    Enter a file name: mbox-short.txt
    stephen.marquard@uct.ac.za
    louis@media.berkeley.edu
    zqian@umich.edu
    [...some output removed...]
    ray@media.berkeley.edu
    cwen@iupui.edu
    cwen@iupui.edu
    cwen@iupui.edu

    There were 27 lines in the file with From as the first word`

**Code Snippet**:

```python
file_name = input(f"Enter File: ")
num = 0

with open('Lecture7/'+file_name,'r') as file:
    lines_list = file.readlines()
    for line in lines_list:
        if line.strip().startswith('From:'):
            print(f"{line.split(" ")[1]}",end='')
            num+=1
    print(f"There were {num} lines in the file with From as the first word")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise7.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-6.png)

### 8. Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.<a name="maximum_minimum"></a>

Exercise 6:
Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the
loop completes.

    `Enter a number: 6
    Enter a number: 2
    Enter a number: 9
    Enter a number: 3
    Enter a number: 5
    Enter a number: done
    Maximum: 9.0
    Minimum: 2.0`

**Code Snippet**:

```python
number = input(f"Enter a number: ")
number_list=[]

while number!='done':
    number_list.append(number)
    number = input(f"Enter a number: ")

maximum = max(number_list)
minimum = min(number_list)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Exercise8.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture7/Screenshots/image-7.png)
