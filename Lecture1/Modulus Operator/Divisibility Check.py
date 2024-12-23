# Check if a number is divisible by another number
x = int(input("Enter the first number (x): "))
y = int(input("Enter the second number (y): "))

if x % y == 0:
    print(f"{x} is divisible by {y}.")
else:
    print(f"{x} is not divisible by {y}. The remainder is {x % y}.")