# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = round(hours * rate, 2)
print(f"Pay = {pay}💸")