#--------------------Operator Exercise Solution----------------

# ===============================
# 1. Arithmetic Operations
# ===============================
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulo:", a % b)
print("Power:", a ** b)
print(10 + 5)       # number + number
print(10 + 5.5)     # number + float
print(10 + True)    # number + boolean
print("Hello" * 3)  # string * number
# print(10 + "5")   # ❌ Error

# ===============================
# 2. Remainder of a number
# ===============================
a = 10
b = 3
print("Remainder:", a % b)

# ===============================
# 3. Area of Circle
# ===============================
pi = 3.14
radius = 10
print("Area:", pi * radius * radius)

# ===============================
# 4. Normal Calculator
# ===============================
a = 20
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# ===============================
# 5. Last Digit of Number
# ===============================
num = 10203
print("Last digit:", num % 10)

# ===============================
# 6. Area of Triangle
# ===============================
base = 10
height = 5
print("Area:", (base * height) / 2)

# ===============================
# 7. Area of Square
# ===============================
side = 6
print("Area:", side * side)

# ===============================
# 8. Area of Rectangle
# ===============================
length = 8
width = 4
print("Area:", length * width)

# ===============================
# 9. Simple Interest
# ===============================
p = 1000
r = 10
t = 1
print("Simple Interest:", (p * r * t) / 100)

# ===============================
# 10. Swap Two Numbers
# ===============================
a, b = 10, 20
a, b = b, a
print("Swap method1:", a, b)

a, b = 10, 20
temp = a
a = b
b = temp
print("Swap method2:", a, b)

a, b = 10, 20
a = a + b
b = a - b
a = a - b
print("Swap method3:", a, b)

# ===============================
# 11. Celsius ↔ Fahrenheit
# ===============================
c = 20
f = (c * 9/5) + 32
print("C to F:", f)
f = 68
c = (f - 32) * 5/9
print("F to C:", c)

# ===============================
# 12. Km ↔ Miles
# ===============================
km = 10
miles = km * 0.621371
print("Km to Miles:", miles)
miles = 6.21
km = miles * 1.60934
print("Miles to Km:", km)

# ===============================
# 13. Cm ↔ Inches
# ===============================
cm = 10
inches = cm * 0.393701
print("Cm to Inches:", inches)
inches = 3.94
cm = inches * 2.54
print("Inches to Cm:", cm)

# ===============================
# 14. Feet ↔ Meters
# ===============================
feet = 10
meters = feet * 0.3048
print("Feet to Meters:", meters)
meters = 3.28
feet = meters * 3.28084
print("Meters to Feet:", feet)

# ===============================
# 15. Pounds ↔ Kg
# ===============================
pounds = 10
kg = pounds * 0.453592
print("Pounds to Kg:", kg)
kg = 4.54
pounds = kg * 2.20462
print("Kg to Pounds:", pounds)

# ===============================
# 16. Cube of Number
# ===============================
num = 10
print("Cube:", num * num * num)
print("Cube (using **):", num ** 3)

# ===============================
# 17. Square Root
# ===============================
num = 100
print("Square Root:", num ** 0.5)

# ===============================
# 18. Gross Salary
# ===============================
basic = 20000
da = 0.40 * basic
hra = 0.20 * basic
gross = basic + da + hra
print("Gross Salary:", gross)

# ===============================
# 19. Compound Assignment
# ===============================
a = 10
a += 10
print("a after += :", a)
a -= 5
print("a after -= :", a)
a *= 2
print("a after *= :", a)
a /= 3
print("a after /= :", a)

# ===============================
# 20. Relational Operation
# ===============================
print(10 > 5)             # number vs number
print("abc" == "abc")     # string vs string
print("5" == 5)           # string vs number
# print(True < "abc")     # ❌ Error in Python

# ===============================
# 21. Logical Operation
# ===============================
x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(10 and 0)
print(10 or 0)

# ===============================
# 22. Bitwise Operation
# ===============================
a = 10   # 1010
b = 4    # 0100
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT a:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
