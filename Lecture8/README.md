![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=23&text=Exercises%20of%20Chapter%208&fontSize=61&animation=twinkling)

Here solutions to the Exercises from Chapter 8 - Dictionary

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/practical.ipynb)

## Table of Contents

1. [Exercise 1](#ex1)
2. [Exercise 2](#ex2)
3. [Exercise 3](#ex3)
4. [Exercise 4](#ex4)
5. [Exercise 5](#ex5)

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise1.py)

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise2.py)

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise3.py)

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise4.py)

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture8/Screenshots/image-4.png)
