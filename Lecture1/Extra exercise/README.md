![header](https://capsule-render.vercel.app/api?type=venom&height=300&color=gradient&customColorList=13&text=Extra%20Exercise&fontColor=ccc)

Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75

Pay: 96.25

## How it Works:

1. The program asks for the number of hours worked.
2. The program asks for the hourly rate.
3. It then calculates the gross pay by multiplying the hours worked by the hourly rate.
4. The program outputs the calculated pay, rounded to two decimal places.

## Code Implementation:

        hours = int(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))

        pay = hours * rate
        print(f"Pay: {pay:.2f}")

![image](https://github.com/user-attachments/assets/d8b5a2aa-f619-4d1e-a3e3-a05cecc7a574)
