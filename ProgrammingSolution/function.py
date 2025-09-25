#-----------------Function Exercise Solution--------------



# 1. Create a function
def hello():
    print("Hello World")
hello()

# 2. Print a message multiple times
def message():
    print("This is a message")
message()
message()
message()

# 3. Add two numbers
def add(a, b):
    return a + b
print(add(5, 3))

# 4. Multiply two numbers
def multiply(a, b):
    return a * b
print(multiply(4, 6))

# 5. Square a number
def square(n):
    return n * n
print(square(7))

# 6. Maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(10, 20))

# 7. Minimum of two numbers
def minimum(a, b):
    if a < b:
        return a
    else:
        return b
print(minimum(10, 20))

# 8. Area of a circle
def area_circle(r):
    pi = 3.14159
    return pi * r * r
print(area_circle(5))

# 9. Area of a rectangle
def area_rectangle(l, w):
    return l * w
print(area_rectangle(10, 6))

# 10. Area of a triangle
def area_triangle(b, h):
    return 0.5 * b * h
print(area_triangle(8, 12))

# 11. Power (a, b)
def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result
print(power(2, 5))

# 12. Convert Year to Roman Numerals
def to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    result = ""
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]
    return result
print(to_roman(1988))
print(to_roman(1525))

# 13. Convert Roman Numerals to Decimal
def from_roman(s):
    values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
            total += values[s[i+1]] - values[s[i]]
            i += 2
        else:
            total += values[s[i]]
            i += 1
    return total
print(from_roman("MCMLXXXVIII"))  # 1988
print(from_roman("MDXXV"))        # 1525

# 14. Recursion - Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# 15. Recursion - Sum of list
def sum_list(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_list(arr, i+1)
print(sum_list([1,2,3,4,5]))

# 16. Recursion - Product of list
def product_list(arr, i=0):
    if i == len(arr):
        return 1
    return arr[i] * product_list(arr, i+1)
print(product_list([1,2,3,4,5]))
