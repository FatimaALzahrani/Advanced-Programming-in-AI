![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=25&text=Chained%20Conditionals&fontSize=61&animation=twinkling)

  ```python
    choice = input("Enter choice: ")
    if choice == 'a':
        print('Bad guess')
    elif choice == 'b':
        print('Good guess')
    elif choice == 'c':
        print('Close, but not Correct')
  ```

### • What do you notice about `else` in the code above?

- The code does not include an `else` block. If the input is not `'a'`, `'b'`, or `'c'`, nothing happens. We can add an `else` block to handle unexpected inputs:

  ```python
  else:
      print('Invalid choice')
  ```

### • In general, is there are limit on the number of `elif` statements?

- There is **no limit** to the number of `elif` statements in Python. We can add as many `elif` statements as needed to check multiple conditions. However, it's important to maintain **readability** and **ease of maintenance** of the code.
