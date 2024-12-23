![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=21&text=Boolean%20Expressions&fontSize=45&animation=twinkling)

## Questions

### 1. What are the differences between == and is ?

### 2. What are the differences between != and is not ?

### 3. What are the differences between = and == ?

<hr>

## Solutions

### 1. `==` vs `is`

- **`==` (Equality operator)**:

  - This operator compares the **values** of two objects. It checks if the values stored in two objects are the same, regardless of whether the objects themselves are the same in memory.
  - It returns `True` if the values are equal, and `False` if they are not.

- **`is` (Identity operator)**:
  - This operator compares the **memory addresses** of two objects. It checks if two variables point to the exact same object in memory.
  - It returns `True` if both variables refer to the same object in memory, and `False` if they refer to different objects, even if the objects themselves are identical.

### 2. `!=` vs `is not`

- **`!=` (Inequality operator)**:

  - This operator compares the **values** of two objects. It checks if the values stored in two objects are different.
  - It returns `True` if the values are not equal, and `False` if the values are the same.

- **`is not` (Identity inequality operator)**:
  - This operator compares the **memory addresses** of two objects. It checks if two variables do not point to the same object in memory.
  - It returns `True` if the two variables refer to different objects in memory, and `False` if they refer to the same object.

### 3. `=` vs `==`

- **`=` (Assignment operator)**:

  - This operator is used to **assign** a value to a variable.
  - It stores the value on the right-hand side into the variable on the left-hand side.

- **`==` (Equality operator)**:
  - This operator is used to **compare** the values of two objects to check if they are equal.
  - It returns `True` if the values are equal, and `False` if they are not.

<hr>

### Summary:

- **`==`** compares values for equality.
- **`is`** checks if two objects are the same in memory.
- **`!=`** checks if values are not equal.
- **`is not`** checks if two objects are not the same in memory.
- **`=`** is used for assigning values to variables.
