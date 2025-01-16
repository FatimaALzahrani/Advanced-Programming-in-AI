# Write a function that takes a tuple of numbers and returns the maximum value.

def max_num(num_tuple):
    mx=num_tuple[0]
    for num in num_tuple:
        if num>mx:
            mx=num
    # mx = max(numbers)
    return mx

if __name__ == '__main__':
    numbers = (1, 2, 3, 4, 5)
    maximum = max_num(numbers)
    print("Max of numbers:", maximum)
