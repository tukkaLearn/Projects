#-------------Object/Dictionary Exercise Solution--------------


# 1. Create an object/dictionary
person = {
    "name": "Sadhu",
    "age": 2,
    "city": "Kashi"
}
print(person)

# 2. Access a value
print(person["name"])
print(person["city"])

# 3. Get all keys
for key in person:
    print(key)

# 4. Get all values
for key in person:
    print(person[key])

# 5. Get all key-value pairs
for key in person:
    print(key, ":", person[key])

# 6. Add a new key-value pair
person["country"] = "India"
print(person)

# 7. Remove a key-value pair
del person["age"]
print(person)

# 8. Check if a key exists
key = "city"
found = False
for k in person:
    if k == key:
        found = True
        break
print("Exists" if found else "Not Exists")

# 9. Count keys
count = 0
for k in person:
    count += 1
print(count)

# 10. Merge two objects
obj1 = {"a": 1, "b": 2}
obj2 = {"c": 3, "d": 4}
merged = {}
for k in obj1:
    merged[k] = obj1[k]
for k in obj2:
    merged[k] = obj2[k]
print(merged)

# 11. Clone an object
clone = {}
for k in person:
    clone[k] = person[k]
print(clone)

# 12. Convert object to list (key-value pairs)
pairs = []
for k in person:
    pairs.append([k, person[k]])
print(pairs)

# 13. Convert list to object
lst = [["name", "Sadhu"], ["age", 2], ["city", "Kashi"]]
obj = {}
for item in lst:
    obj[item[0]] = item[1]
print(obj)

# 14. Highest value
data = {"a": 10, "b": 20, "c": 5}
max_key = None
max_val = -999999
for k in data:
    if data[k] > max_val:
        max_val = data[k]
        max_key = k
print("Key:", max_key, "Value:", max_val)

# 15. Update value in nested object
nested = {"person": {"name": "John", "age": 30}}
nested["person"]["age"] = 40
print(nested)

# 16. Delete key in nested object
del nested["person"]["name"]
print(nested)

# 17. Swap key and value
d = {"a": 1, "b": 2}
swapped = {}
for k in d:
    v = d[k]
    swapped[v] = k
print(swapped)

# 18. Count frequency from list
arr = [1, 2, 2, 3]
freq = {}
for x in arr:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1
print(freq)
