#------------------File Exercise Solution----------------

# 1. File Read
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)


# 2. File Write
with open("output.txt", "w") as f:
    f.write("Hello, this is a test write.\n")


# 3. File Append
with open("output.txt", "a") as f:
    f.write("This line is appended.\n")


# 4. Write Multiple Lines to a File (from a list)
lines = ["Mark", "Sadhu", "Python", "Practice"]
with open("list.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")


# 5. Sorted order by name
with open("students.txt", "r") as f:
    students = [line.strip().split(",") for line in f]
students.sort(key=lambda x: x[0])  # sort by name
for name, age in students:
    print(name, age)


# 6. Sorted order by age
with open("students.txt", "r") as f:
    students = [line.strip().split(",") for line in f]
students.sort(key=lambda x: int(x[1]))  # sort by age
for name, age in students:
    print(name, age)


# 7. Copy a File Data to Another File (convert to uppercase)
with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())


# 8. Merge lines alternately from 2 files
with open("file1.txt") as f1, open("file2.txt") as f2, open("merged.txt", "w") as out:
    while True:
        l1 = f1.readline()
        l2 = f2.readline()
        if not l1 and not l2:
            break
        if l1: out.write(l1)
        if l2: out.write(l2)


# 9. Encrypt / Decrypt File
# 9.1 Caesar Cipher (shift by 3)
def caesar_encrypt(text, shift=3):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
        else:
            result += ch
    return result

with open("plain.txt", "r") as f, open("cipher.txt", "w") as out:
    for line in f:
        out.write(caesar_encrypt(line))


# 9.2 Substitution Cipher
sub_map = {
    "A": "!", "B": "5", "C": "#", "D": "$", 
    "E": "@", "F": "&", "G": "%", "H": "?", 
    "I": "*", "J": "+", "K": "-", "L": "=", 
    "M": ">", "N": "<", "O": "0", "P": "1", 
    "Q": "2", "R": "3", "S": "4", "T": "6", 
    "U": "7", "V": "8", "W": "9", "X": "[", 
    "Y": "]", "Z": "^"
}
def substitute_encrypt(text):
    result = ""
    for ch in text.upper():
        result += sub_map.get(ch, ch)  # if not in map, keep same
    return result

with open("plain.txt", "r") as f, open("sub_cipher.txt", "w") as out:
    for line in f:
        out.write(substitute_encrypt(line))
