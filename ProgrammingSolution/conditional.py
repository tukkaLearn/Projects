#---------------Conditional Exercise Solution----------------

# 1. Positive, Negative or Zero
num = -5
if num > 0:
    print("Positive")
if num < 0:
    print("Negative")
if num == 0:
    print("Zero")

# 2. Even or Odd
num = 11
if num % 2 == 0:
    print("Even")
if num % 2 != 0:
    print("Odd")

# 3. Leap Year
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 4. Vowel or Consonant
ch = "Hello"
if "a" in ch or "e" in ch or "i" in ch or "o" in ch or "u" in ch or "A" in ch or "E" in ch or "I" in ch or "O" in ch or "U" in ch:
    print("Vowel")
else:
    print("Consonant")

# 5. Largest Number
a, b, c = 10, 25, 15
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 6. Smallest Number
a, b, c = 10, 25, 15
if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)

# 7. Discount Calculator
qty = 1200
price = 10
total = qty * price
if qty > 1000:
    total = total - (total * 0.10)
print("Total Expense:", total)

# 8. Voting System
age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# 9. Grading System
marks = 72
if 80 <= marks <= 100:
    print("Grade A")
elif 60 <= marks <= 79:
    print("Grade B")
elif 40 <= marks <= 59:
    print("Grade C")
elif 33 <= marks <= 39:
    print("Grade D")
else:
    print("Grade F")

# 10. Divisibility Test
num = 55
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")

# 11. Divisibility Test and Operations
num = 9
if num % 2 == 0:
    num *= 2
elif num % 3 == 0:
    num *= 3
else:
    num -= 1
print("Result:", num)

# 12. Range of Numbers
n = 45
if 0 <= n <= 10:
    print("Low")
elif 11 <= n <= 50:
    print("Medium")
elif 51 <= n <= 100:
    print("High")
else:
    print("Out of range")

# 13. Profit or Loss Calculator
cp = 150
sp = 200
if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No Profit No Loss")

# 14. Triangle validity
a1, a2, a3 = 60, 60, 60
if a1 + a2 + a3 == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# 15. Print Month Name
# Method 1
month = 4
if month == 1: print("Jan")
elif month == 2: print("Feb")
elif month == 3: print("Mar")
elif month == 4: print("Apr")
elif month == 5: print("May")
elif month == 6: print("Jun")
elif month == 7: print("Jul")
elif month == 8: print("Aug")
elif month == 9: print("Sep")
elif month == 10: print("Oct")
elif month == 11: print("Nov")
elif month == 12: print("Dec")
else: print("Invalid Month")

# Method 2 
month =4
match month:
    case 1: print("Jan")
    case 2: print("Feb")
    case 3: print("Mar")
    case 4: print("Apr")
    case 5: print("May")
    case 6: print("Jun")
    case 7: print("Jul")
    case 8: print("Aug")
    case 9: print("Sep")
    case 10: print("Oct")
    case 11: print("Nov")
    case 12: print("Dec")
    case _: print("Invalid Month")


# 16. Vending Machine (nested if in place of switch)
category = 2
item = 1
if category == 1:
    if item == 1:
        print("Chips")
    elif item == 2:
        print("Chocolate")
elif category == 2:
    if item == 1:
        print("Soda")
    elif item == 2:
        print("Juice")
else:
    print("Invalid Choice")

# 17. Company Insurance
married = False
gender = "male"
age = 32
if married:
    print("Insured")
elif not married and gender == "male" and age > 30:
    print("Insured")
elif not married and gender == "female" and age > 25:
    print("Insured")
else:
    print("Not Insured")

# 18. Character Check
ch = "#"
if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Symbol")

# 19. RGB to CMYK
R, G, B = 0, 0, 0
if R == 0 and G == 0 and B == 0:
    C, M, Y, K = 0, 0, 0, 1
else:
    white = max(R/255, G/255, B/255)
    C = (white - (R/255)) / white
    M = (white - (G/255)) / white
    Y = (white - (B/255)) / white
    K = 1 - white
print("CMYK:", C, M, Y, K)

# 20. Login System
username = "admin"
password = "password"
if username == "admin" and password == "password":
    print("Login successful")
else:
    print("Login failed")
