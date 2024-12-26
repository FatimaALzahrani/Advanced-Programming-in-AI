![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=9&text=Catching%20Exceptions&fontSize=61&animation=twinkling)

    ```python
    try:
        x = int(input("Enter a number: "))
        print(10/x)

    except:
        print("Invalid input")
    ```

### • There are two blocks defined with '`try`' and '`except`' keywords. Under what circumstances does each block execute?

- **`try` block**: This block of code runs first. It attempts to execute the code inside it. If no error occurs, the code continues normally.
- **`except` block**: If an error (exception) occurs inside the `try` block, the code execution moves to the `except` block, handling the error and preventing the program from crashing.

### • What is the term used to describe the process of handling an exception with a '`try`' statement in Python programming?

The term used is **Exception Handling**. It allows the program to handle errors gracefully without crashing.

### • How does catching an exception with a '`try`' statement operate, and what actions can be taken when an exception is caught as illustrated in the given example?

- When an error occurs in the `try` block, the program moves to the `except` block. This prevents the program from crashing and provides a way to handle the error.
- Actions that can be taken:
  - Display an error message to the user.
  - Log the error.
  - Perform any necessary recovery or cleanup actions.
