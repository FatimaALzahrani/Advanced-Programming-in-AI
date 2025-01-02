![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=13&text=Exercises&fontSize=70&animation=twinkling)

Here solutions to the Exercises from Chapter 5 - Strings

To reach the practical application during the lecture [Click here](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/practical.ipynb)

## Chapter Exercises

1. [Write a program to count the occurrences of a character in a string.](#count_character)
2. [Write a program to reverse a string using slicing.](#reverse_string)
3. [Extract the domain name from an email address.](#extract_domian)
4. [Split a string into words and count their occurrences.](#split_strings)
5. Do the exercises on pages 76 and 77 of the book
   - [Slicing strings](#Slicing)
   - [String methods](#methods)

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

## 5. Slicing strings <a name="Slicing"></a>

Take the following Python code that stores a string:

```python
   str = X-DSPAM-Confidence: 0.8475
```

Use `find` and string `slicing` to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

**Code Snippet**:

```python
def  extract_float(s):
    index = s.find(':')+1
    return float(s[index:].strip())

s = 'X-DSPAM-Confidence: 0.8475'
f = extract_float(s)
print(f)
```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise5.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-6.png)

## 6. String methods <a name="methods"></a>

Read the documentation of the string methods at [https://docs.python.org/library/stdtypes.html#string-methods](https://docs.python.org/library/stdtypes.html#string-methods).
You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.
The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

### **1. Using `strip()` to Clean Up Whitespace**

```python
# Removing leading and trailing spaces
dirty_string = "   Hello, World!   "
clean_string = dirty_string.strip()
print(f"Before strip: '{dirty_string}' | After strip: '{clean_string}'")
```

### **2. Using `replace()` to Replace Substrings**

```python
# Replacing a substring
text = "I love Python programming"
new_text = text.replace("Python", "AI")
print(f"Before replace: '{text}' | After replace: '{new_text}'")
```

### **3. Using `find()` to Locate a Substring**

```python
# Finding the position of a substring
sentence = "The quick brown fox jumps over the lazy dog."
position = sentence.find("fox")
print(f"The word 'fox' is found at index: {position}")
```

### **4. `strip()` & `replace()`**

```python
# Cleaning and replacing in one go
dirty_text = "   The sky is blue   "
clean_replaced_text = dirty_text.strip().replace("blue", "clear")
print(f"Result: '{clean_replaced_text}'")
```

### \*\*\*\*

```python

```

### \*\*\*\*

```python

```

### \*\*\*\*

```python

```

**Solution**: [See Full Code](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Exercise6.py)

**Screenshot from the output**:
![alt text](https://github.com/FatimaALzahrani/Advanced-Programming-in-AI/blob/main/Lecture5/Screenshots/image-7.png)
