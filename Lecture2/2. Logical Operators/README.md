![header](https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=22&text=Logical%20Operators&fontSize=61&animation=twinkling)

### 17 and True

**Why the output is True?**

In Python, the `and` operator evaluates both operands. If both operands are truthy, it returns the second operand. Since:

- `17` is a non-zero number, which is considered `True` in Python.
- `True` is obviously truthy.

The expression `17 and True` returns `True`.

#### Example in `try.py` file:

        def demonstrate_and_operator(value1, value2):
            result = value1 and value2  # The 'and' operator returns the second operand if both are truthy
            print(f"Result of {value1} and {value2}: {result}")

        demonstrate_and_operator(17, True)
        # Expected output: True
