![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=25&text=Exercises%20of%20Chapter%209&fontSize=61&animation=twinkling)

Here solutions to the Exercises from Chapter 9 - Tuples

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/practical.ipynb)

## Table of Contents

1. [Exercise 1](#ex1)
2. [Exercise 2](#ex2)
3. [Exercise 3](#ex3)

### Exercise 1: <a name="ex1"></a>

Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:

    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5
    Enterafilename: mbox.txt
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

def list_tuple(dictionary):
    list_emails = []
    for d in dictionary:
        list_emails.append((d,dictionary[d]))
    list_emails.sort(reverse=True, key=lambda x: x[1])
    return list_emails
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Screenshots/image.png)

### Exercise2: <a name="ex2"></a>

This program counts the distribution of the hour of the day for each of the messages.You can pull the hour from the “From” line by finding the time
string and then split ting that string into parts using the colon character. Once you have accumulated the counts for each hour,print out the counts,one perline, sorted by hour as shown below

    python timeofday.py
    Enter a file name: mbox-short.txt
    04 3
    06 1
    07 1
    09 2
    10 3
    11 6
    14 1
    15 2
    16 4
    17 2
    18 1
    19 1

**Code Snippet**:

```python
def hours(file):
    dictionary={}
    with open('Lecture9/'+file,'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('From '):
                email = line.split()[5].split(':')
                dictionary[email[0]] = 1 if email[0] not in dictionary else dictionary[email[0]]+1
        return dictionary

if __name__ == '__main__':
    file_name = input(f"Enter File name : ")
    dictionary = hours(file_name)
    list_tuple = sorted(dictionary.items(), key=lambda x: x[0], reverse=False)
    for hour,count in list_tuple:
        print(f"{hour} {count}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Screenshots/image-1.png)

### Exercise3: <a name="ex3"></a>

Write a program that reads a file and prints the letters in decreasing order of frequency.
Your program should convert all the input to lower case and only count the letters a-z.
Your program should not count spaces, digits, punctuation, or any thing other than the letters a-z.
Find text samples from several different languages and see how letter frequency varies between languages.
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies

**Code Snippet**:

```python
def letter_freq(file_name):
    letter_counts = {}

    with open('Lecture8/'+file_name, 'r') as file:
        for line in file:
            line = line.lower()
            for char in line:
                if 'a' <= char <= 'z':
                    letter_counts[char] = letter_counts.get(char, 0) + 1

    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_letter_counts:
        print(f"{letter}: {count}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Screenshots/image-2.png)
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture9/Screenshots/image-3.png)
