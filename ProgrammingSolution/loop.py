# -------------------Loop Exercise Solution----------------

# 1. Print numbers from 1 to 10
num=1
while num <= 10:
    print(num)
    num += 1

# 2. Print even numbers from 1 to 100
# Method 1
num=2
while num <= 100:
    print(num)
    num += 2

# Method 2
num=2
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1

# 3. Print odd numbers from 1 to 100
# Method 1
num=1
while num <= 100:
    print(num)
    num += 2

# Method 2
num=1
while num <= 100:
    if num % 2 != 0:
        print(num)
    num += 1

# 4. Print squares of numbers from 1 to 10
num=1
while num <= 10:
    print(num*num)
    num += 1

# 5. Print Table of a Number from 1 to 10
num = int(input("Enter number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1

# 6. Count total number of digits
n = int(input("Enter number: "))
count = 0
while n > 0:
    n //= 10
    count += 1
print("Digits:", count)

# 7. Reverse of a number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print("Reverse:", rev)

# 8. Sum of digits
n = int(input("Enter number: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum:", s)

# 9. Factorial of a number
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# 10. Fibonacci series
n = int(input("Enter terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b

# 11. Prime factors
n = int(input("Enter number: "))
i = 2
while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n //= i
    else:
        i += 1

# 12. Palindrome or not
n = int(input("Enter number: "))
temp, rev = n, 0
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
print("Palindrome" if rev == n else "Not Palindrome")

# 13. Sum of odd numbers 1–100
s = 0
for i in range(1, 101, 2):
    s += i
print("Sum odd:", s)

# 14. Sum of even numbers 1–100
s = 0
for i in range(2, 101, 2):
    s += i
print("Sum even:", s)

# 15. Sum of all numbers 1–100
s = 0
for i in range(1, 101):
    s += i
print("Sum all:", s)

# 16. Prime or not
# Method 1
n = int(input("Enter number: "))
is_prime = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print("Prime")
else:
    print("Not Prime")


# 17. All primes 1–100
for n in range(2, 101):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            break
    else:
        print(n, end=" ")

# 18. Sum of primes 1–100
s = 0
for n in range(2, 101):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            break
    else:
        s += n
print("Sum primes:", s)

# 19. Armstrong or not
n = int(input("Enter number: "))
temp, s = n, 0
while temp > 0:
    d = temp % 10
    s += d**3
    temp //= 10
print("Armstrong" if s == n else "Not Armstrong")

# 20. Count positives, negatives, zeros
pos = neg = zero = 0
while True:
    n = int(input("Enter number (999 to stop): "))
    if n == 999:
        break
    if n > 0: pos += 1
    elif n < 0: neg += 1
    else: zero += 1
print("Positive:", pos, "Negative:", neg, "Zeros:", zero)

# 21. Range of numbers
nums = []
while True:
    n = int(input("Enter number (999 to stop): "))
    if n == 999:
        break
    nums.append(n)
print("Range:", max(nums)-min(nums))

# 22. Sum of series 1/1! + ... + 7/7!
import math
s = 0
for i in range(1, 8):
    s += i / math.factorial(i)
print("Sum:", s)

# 23. All combinations of 1,2,3
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            print(i, j, k)

# 24. Intelligence table
for y in range(1, 7):
    x = 5.5
    while x <= 12.5:
        i = 2 + (y + 0.5*x)
        print("y=", y, "x=", x, "i=", i)
        x += 0.5

# 25. Pythagorean triplets ≤ 30
for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a*a + b*b == c*c:
                print(a, b, c)

# 26. Patterns
# 1.
for i in range(1, 6):
    print("*"*i)

# 2.
for i in range(1, 6):
    print(" "*(5-i), "* "*i)

# 3.
for i in range(1, 6):
    print((str(i)+" ")*i)

# 4.
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 5.
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 6.
for i in range(1, 6):
    for j in range(65, 65+i):
        print(chr(j), end=" ")
    print()

# 7.
ch = 65
for i in range(1, 6):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

# 8.
ch, num = 65, 1
for i in range(1, 6):
    for j in range(i):
        print(str(num)+chr(ch), end=" ")
        ch += 1
        num += 1
    print()

# 9.
ch = 65
for i in range(1, 6):
    print(" "*(5-i), end="")
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

# 10.
for i in range(1, 6):
    print(" "*(5-i), "* "*i)

# 11.
for i in range(1, 8):
    for j in range(1, 8):
        if j <= i and j <= 4 or j >= 8-i and j >= 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
