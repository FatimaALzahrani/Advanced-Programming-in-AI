# Do the exercises on pages 64 and 65 of the book (Charles R. Severance .et al, Python for Everybody: Exploring Data in Python 3, CreateSpace Independent Publishing Platform, 2024).

#  Exercise 5: What will the following Python program print out?
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()

"""
Answer:
d) ABC Zap ABC
The program calls jane() which prints "ABC", then fred() which prints "Zap", and then jane() again prints "ABC".
"""