# Do the exercises on pages 64 and 65 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024).

#  Exercise 4: What is the purpose of the “def” keyword in Python?
#  a) It is slang that means “the following code is really cool”
#  b) It indicates the start of a function
#  c) It indicates that the following indented section of code is to be stored for later
#  d) b and c are both true
#  e) None of the above

# Define a function using the 'def' keyword
def greet(name):
    """
    This function takes a name as an argument and prints a greeting message.
    """
    print(f"Hello, {name}! Welcome to Python.")

# Call the function
greet("Mohammed")  # Output: Hello, Mohammed! Welcome to Python.
greet("Fatimah") # Output: Hello, Fatimah! Welcome to Python.

"""
The def keyword begins the function definition.
greet is the function name.
(name) is the parameter the function accepts.
The indented code block is the body of the function, which executes when the function is called.
greet("Mohammed") and greet("Fatimah") are function calls that execute the function with different arguments.
"""