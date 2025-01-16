# Create a tuple with numbers and find the sum using a loop.

def tuple_sum(numbers):
    total = 0
    #1. Using a loop to calculate the sum
    for number in numbers:
        total += number
    #2. Using Built-in function sum
    # total = sum(numbers)
    return total

if __name__ == '__main__':
    numbers = (1, 2, 3, 4, 5)
    total = tuple_sum(numbers)
    print("Sum of numbers:", total)
