![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=23&text=Exercises%20of%20Chapter%208&fontSize=61&animation=twinkling)

Here solutions to the Exercises from Chapter 8 - Dictionary

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/practical.ipynb)

## Table of Contents

1.  [Create a dictionary representing a student's data (name, age, subjects).](#ex1_1)
2.  [Write a program to count the frequency of words in a string using a dictionary.](#ex1_2)
3.  [Merge two dictionaries into one.](#ex1_3)
4.  [Access and print data from a nested dictionary.](#ex1_4)
5.  [Book Exercises](#book)
    - [Exercise 1](#ex1)
    - [Exercise 2](#ex2)
    - [Exercise 3](#ex3)
    - [Exercise 4](#ex4)
    - [Exercise 5](#ex5)

### 1. Create a dictionary representing a student's data (name, age, subjects). <a name="ex1_1"></a>

**Code Snippet**:

```python
students = {'1':{'name':'Fatimah Alzahrani','age':22,'subjects':['Advanced Programming in AI','Advanced Statistics and Probability']},
            '2':{'name':'Ahmed Alzahrani','age':9,'subjects':['Math','Sciences','Artistic']},
            '3':{'name':'Majd Alzahrani','age':22,'subjects':['Data visualization','Object Oriented Programming','Robots']}}
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-ex1.png)

<hr/>

### 2. Write a program to count the frequency of words in a string using a dictionary. <a name="ex1_2"></a>

**Code Snippet**:

```python
def count_words(text):
    dictionary={}
    words=text.split(' ')
    for word in words:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
    return dictionary
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-ex2.png)

<hr/>

### 3. Merge two dictionaries into one. <a name="ex1_3"></a>

**Code Snippet**:

```python
personal_info = {
    "employee_id": 1,
    "full_name": "Fatimah Alzahrani",
    "age": 22,
    "email": "12fatimah.15@gmail.com"
}

work_info = {
    "position": "Software Engineer",
    "department": "Technology",
    "salary": 85000,
    "hire_date": "2025-01-16"
}

employee_profile = {**personal_info, **work_info}
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-ex3.png)

<hr/>

### 4. Access and print data from a nested dictionary. <a name="ex1_4"></a>

**Code Snippet**:

```python
employee_data = {
    "employee_1": {
        "name": "Fatimah Mohammed",
        "age": 22,
        "contact_info": {
            "email": "12fatimah.15@gmail.com",
            "phone": "1234567890"
        },
        "work_info": {
            "position": "Software Engineer",
            "department": "Technology",
            "salary": 85000
        }
    },
    "employee_2": {
        "name": "Mohammed Abduallah",
        "age": 50,
        "contact_info": {
            "email": "Mohammed@gmail.com",
            "phone": "1234567890"
        },
        "work_info": {
            "position": "Project Manager",
            "department": "Operations",
            "salary": 95000
        }
    }
}

for employee_key, employee in employee_data.items():
    print("=" * 50)
    print(f"{employee_key.replace('_', ' ').title()}:")
    print(f"Name: {employee['name']}")
    print(f"Email: {employee['contact_info']['email']}")
    print(f"Position: {employee['work_info']['position']}")
    print(f"Department: {employee['work_info']['department']}")
    print(f"Salary: ${employee['work_info']['salary']:,}")
    print("=" * 50)
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-ex4.png)

<hr/>

## Book%20Exercises <a name="book"></a>

### Exercise 1: Download a copy of the file <a name="ex1"></a>

[www.py4e.com/code3/words.txt](www.py4e.com/code3/words.txt)
Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

**Code Snippet**:

```python
def read_words(file):
    dic = {}
    with open('Lecture8/'+file,'r') as file:
        words = re.split(r'[\n\s]+', file.read())
        for word in words:
            dic[word]=''
    return dic

def check_string(dictionary,word):
    return word in dictionary
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Book%20Exercises/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image.png)

### Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. <a name="ex2"></a>

To do this look or lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

**Sample Line:**

    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

**Sample Execution:**

    python dow.py
    Enter a file name: mbox-short.txt
    {Fri: 20, Thu: 6, Sat: 1}

**Code Snippet**:

```python
def days(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()
                dictionary[email[2]] = 1 if email[2] not in dictionary else dictionary[email[2]]+1
        return dictionary
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Book%20Exercises/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-1.png)

### Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary. <a name="ex3"></a>

    Enter file name: mbox-short.txt
    {gopal.ramasammycook@gmail.com: 1, louis@media.berkeley.edu: 3,
    cwen@iupui.edu: 5, antranig@caret.cam.ac.uk: 1,
    rjlowe@iupui.edu : 2, gsilver@umich.edu: 3,
    david.horwitz@uct.ac.za: 4, wagnermr@iupui.edu: 1,
    zqian@umich.edu: 4, stephen.marquard@uct.ac.za: 2,
    ray@media.berkeley.edu: 1}

**Code Snippet**:

```python
def emails(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()
                dictionary[email[1]] = 1 if email[1] not in dictionary else dictionary[email[1]]+1
        return dictionary
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Book%20Exercises/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-2.png)

### Exercise 4: Add code to the above program to figure out who has the most messages in the file. <a name="ex4"></a>

After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5
    Enter a file name: mbox.txt
    zqian@umich.edu 195

**Code Snippet**:

```python
def emails(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()
                dictionary[email[1]] = 1 if email[1] not in dictionary else dictionary[email[1]]+1
        return dictionary

def maximum(emails):
    largest = None
    em = None
    for email in emails:
        if largest == None or emails[email]>largest:
            largest = emails[email]
            em = email
    return largest,em
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Book%20Exercises/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-3.png)

### Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). <a name="ex5"></a>

At the end of the program, print out the contents of your dictionary.

    python schoolcount.py
    Enter a file name: mbox-short.txt
    {media.berkeley.edu: 4, uct.ac.za: 6, umich.edu: 7,
    gmail.com: 1, caret.cam.ac.uk: 1, iupui.edu: 8}

**Code Snippet**:

```python
def domains(file):
    dictionary={}
    with open('Lecture8/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()[1].split('@')
                dictionary[email[1]] = 1 if email[1] not in dictionary else dictionary[email[1]]+1
        return dictionary
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Book%20Exercises/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-4.png)
