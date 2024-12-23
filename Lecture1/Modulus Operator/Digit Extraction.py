# Extract the right-most digit and last two digits of a number
x = int(input("Enter a number: "))

right_most_digit = x % 10
last_two_digits = x % 100

print(f"Right-most digit: {right_most_digit}")
print(f"Last two digits: {last_two_digits}")