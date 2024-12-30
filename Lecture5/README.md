![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=13&text=Exercises&fontSize=70&animation=twinkling)

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/practical.ipynb)

## Chapter Exercises

1. [Write a program to count the occurrences of a character in a string.](#count_character)
2. [Write a program to reverse a string using slicing.](#reverse_string)
3. [Extract the domain name from an email address.](#extract_domian)
4. [Split a string into words and count their occurrences.](#split_strings)
5. Do the exercises on pages 76 and 77 of the book
   - [ Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.](#repeatedly)
   - [Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.](#list_num)

## 1. Write a program to count the occurrences of a character in a string. <a name="count_character"></a>

**Code Snippet**:

```python
def count_character_occurrences(string, char):
    count = string.count(char)
    return count
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise1.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image.png)

## 2. Write a program to reverse a string using slicing. <a name="reverse_string"></a>

**Code Snippet**:

```python
def reverse_string(string):
    reversed_string = string[::-1]
    print(f"Reversed string using slicing: {reversed_string}")
```

#### `string[::-1]` is a slicing operation:

- `:` specifies the entire range of the string.
- `-1` as the step indicates traversal in reverse order.

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise2.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-1.png)

## 3. Extract the domain name from an email address. <a name="extract_domian"></a>

**Code Snippet**:

```python
def extract_domain(email):
    domain = email.split("@")[1]
    # domain = email.split('@')[-1]
    return domain
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise3.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-2.png)

## 4. Split a string into words and count their occurrences. <a name="split_strings"></a>

**Code Snippet**:

```python
def words_count(string):
    words = string.split(" ")
    print("Word occurrences:")
    for i in range(len(words)):
        word = words[i]
        if word not in words[:i]:
            count = 0
            for w in words:
                if w == word:
                    count += 1
            print(f"{word}: {count}")
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise4.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-3.png)

## 5. Write a program which repeatedly reads integers until the user enters “done”. <a name="repeatedly"></a>

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-4.png)

## 6. prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers <a name="list_num"></a>

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

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise6.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-5.png)
