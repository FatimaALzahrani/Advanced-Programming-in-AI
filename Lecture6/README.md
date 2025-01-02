![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=22&text=Files%20Exercises&fontSize=70&animation=twinkling)

Here solutions to the Exercises from Chapter 6 - Files

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/practical.ipynb)

## Chapter Exercises

1. [Write a program to read and print the contents of a text file.](#read)
2. [Write a program to count the number of lines in a file.](#count)
3. [Modify the program to handle errors when the file is missing.](#handle)
4. [Write a program to append new data to an existing file.](#append)
5. Do the exercises on pages 89 and 90 of the book
   - [Exercise 5: Write a program to read through a file and print the contents of the file (line by line) all in upper case.](#upper)
   - [Exercise 6: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475](#avg)
   - [Exercise 7: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in he exact file name “na na boo boo”.](#Egg)

## 1. Write a program to read and print the contents of a text file. <a name="read"></a>

**Code Snippet**:

```python
with open('Lecture6/Mohammed.txt','r') as file:
    print(f"{file.read()}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image.png)

## 2. Write a program to count the number of lines in a file. <a name="count"></a>

**Code Snippet**:

```python
file = open('Lecture6/Mohammed.txt','r')
file_lines = file.readlines()
file.close()
print(f"Number of lines in Mohammed file is : {len(file_lines)}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image-1.png)

## 3. Modify the program to handle errors when the file is missing. <a name="handle"></a>

**Code Snippet**:

```python
try:
    with open('Lecture6/Mohammed.txt','r')as file:
        file_lines = file.readlines()
        print(f"Number of lines in Mohammed file is : {len(file_lines)}")
except FileNotFoundError:
    print(f"File is missing!")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image-3.png)

## 4. Write a program to append new data to an existing file. <a name="append"></a>

**Code Snippet**:

```python
with open('Lecture6/Mohammed.txt','a+') as file:
    file.writelines("Mohammed was born around 570, AD in Mecca (now in Saudi Arabia).\nHis father died before he was born and he was raised first by his grandfather and then his uncle.\nHe belonged to a poor but respectable family of the Quraysh tribe.\nThe family was active in Meccan politics and trade.")
    file.seek(0)
    print(file.read())
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image-2.png)

## Exercise 5: Write a program to read through a file and print the contents of the file (line by line) all in upper case. <a name="upper"></a>

**Code Snippet**:

```python
file_name=input(f"Enter a file name: ")

with open('Lecture6/'+file_name) as file:
    lines=file.readlines()
    for line in lines:
        print(f"{line.upper()}",end='')
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image-4.png)

## 6. Exercise 6: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475 <a name="avg"></a>

**Code Snippet**:

```python
file_name=input(f"Enter a file name: ")
total=0
count=0

with open('Lecture6/'+file_name,'r') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if(line.startswith('X-DSPAM-Confidence:')):
            index=line.find(':')+1
            f=float(line[index:].strip())
            total+=f
            count+=1
    avg=total/count
    print(f"Average spam confidence: {avg}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise6.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image-5.png)

## 7. Exercise 7: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in he exact file name “na na boo boo”. <a name="Egg"></a>

**Code Snippet**:

```python
file_name=input(f"Enter the file name: ")

try:
    with open('Lecture6/'+file_name,'r') as file:
        subject_count = sum(1 for line in file if line.startswith("Subject"))
        print(f"There were {subject_count} subject lines in {file_name}")
except FileNotFoundError:
    if(file_name=='na na boo boo'):
        print(f"NA NA BOO BOO TO YOU- You have been punkd!")
    else:
        print(f"File cannot be opened: {file_name}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Exercise7.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture6/Screenshots/image-6.png)
