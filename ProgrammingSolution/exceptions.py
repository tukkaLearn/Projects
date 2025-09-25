#-------------Exception Handling Exercise Solution--------------

# 1. Throw Exception
try:
    raise Exception("This is a custom exception")
except Exception as e:
    print("Caught Exception:", e)


# 2. Handle Exception
try:
    x = int("abc")   # invalid conversion
except ValueError as e:
    print("Handled ValueError:", e)


# 3. Negative Number Exception
def check_negative(n):
    if n < 0:
        raise Exception("Number cannot be negative")
    else:
        print("Valid number:", n)

try:
    check_negative(-5)
except Exception as e:
    print("Caught Exception:", e)


# 4. Zero Division Exception
def divide(a, b):
    if b == 0:
        raise Exception("Denominator cannot be zero")
    return a / b

try:
    print(divide(10, 0))
except Exception as e:
    print("Caught Exception:", e)
