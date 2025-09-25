#---------List/Array Exercise Solution---------------

# 1. Print all numbers
arr = [5, 2, 4, 10, 5, 1]
for x in arr:
    print(x, end=" ")
print()

# 2. Print even numbers
arr = [3, 10, 5, 2, 12, 7]
for x in arr:
    if x % 2 == 0:
        print(x, end=" ")
print()

# 3. Print odd numbers
arr = [1, 2, 3, 4, 5]
for x in arr:
    if x % 2 != 0:
        print(x, end=" ")
print()

# 4. Print prime numbers
arr = [12, 65, 2, 3, 4, 5, 10, 17, 19]
for x in arr:
    if x > 1:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
        if prime:
            print(x, end=" ")
print()

# 5. Sum of all elements
arr = [1, 2, 3, 4, 5]
total = 0
for x in arr:
    total += x
print(total)

# 6. Maximum element
arr = [2, 1, 10, 11, 15, 0, 14]
maximum = arr[0]
for x in arr:
    if x > maximum:
        maximum = x
print(maximum)

# 7. Minimum element
minimum = arr[0]
for x in arr:
    if x < minimum:
        minimum = x
print(minimum)

# 8. Average
arr = [10, 1, 5, 3, 6, 0, 14]
total = 0
count = 0
for x in arr:
    total += x
    count += 1
avg = total / count
print(round(avg, 2))

# 9. First, Middle, Last
arr = [10, 20, 30, 40, 50, 60, 70]
n = len(arr)
print(arr[0], arr[n//2], arr[n-1])

# 10. Frequency of element
arr = [10, 19, 1, 2, 3, 3, 4, 5]
target = 3
count = 0
for x in arr:
    if x == target:
        count += 1
print(count)

# 11. Reverse a list
arr = [18, 8, 12, 1, 0, 4, 19]
rev = []
for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])
print(rev)

# 12. Sort a list (Bubble Sort)
arr = [4, 3, 2, 2, 1, 5, 0]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# 13. Second Largest
arr = [1, 2, 10, 5, 4, 10, 6, 7]
largest = second = -999999
for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif x > second and x != largest:
        second = x
print(second)

# 14. Second Smallest
smallest = second = 999999
for x in arr:
    if x < smallest:
        second = smallest
        smallest = x
    elif x < second and x != smallest:
        second = x
print(second)

# 15. Search element
arr = [10, 20, 30, 40, 50]
target = 30
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break
print(index)

# 16. Merge two arrays
a1 = [1, 2, 3]
a2 = [4, 5, 6]
merged = []
for x in a1:
    merged.append(x)
for x in a2:
    merged.append(x)
print(merged)

# 17. Intersection of two arrays
a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 6, 7]
inter = []
for x in a1:
    for y in a2:
        if x == y and x not in inter:
            inter.append(x)
print(inter)

# 18. Union of two arrays
a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 6, 7]
union = []
for x in a1:
    if x not in union:
        union.append(x)
for y in a2:
    if y not in union:
        union.append(y)
print(union)

# 19. Difference of two arrays (A1 - A2)
a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 6, 7]
diff = []
for x in a1:
    found = False
    for y in a2:
        if x == y:
            found = True
            break
    if not found:
        diff.append(x)
print(diff)
