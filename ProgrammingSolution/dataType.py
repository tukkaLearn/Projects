# ---------------Data Type Exercise Solution----------------

# 1
name = "Sadhu"
address = "Kashi"
print(name)
print(address)

# -----------------------

# 2 Pattern

# Method 1

print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/")

print("*")
print("**")
print("***")
print("****")

print("    *")
print("   * *")
print("  * * *")
print(" * * * *")

# Method 2

print(r"/\/\/\/\/\/\/\/")
print("*\n**\n***\n*****")
print("      *\n     * *\n    * * *\n   * * * *")

# -------------------------------

# 3 Print Escape Sequence

# Method 1
print("\\n\\n\\n\\n\\n\\n\\n")
print('\\t\\\"\\\'\\n\\t')

# Method 2
print(r"\n\n\n\n\n\\n\n")
print(r"\t\"\'\n\t")



# 4. Integer data type
a = 10
b = 20
print(a, b)         # 10 20
a = 0b101010
print(a)            # Binary → 42
a = 0o101010
print(a)            # Octal
a = 0x101010
print(a)            # Hexadecimal

# 5. Float data type
a = 10.020
print(a)
b = 20.
print(b)
a = 10e3
print(a)            # 10000.0
a = 2e10
print(a)            # 20000000000.0
a = 5e-3
print(a)            # 0.005

# 6. Complex data type
a = 10 + 3j
b = 2.0 + 1j
c = 2 + 0j
print(a, "Real:", a.real, "Imag:", a.imag)
print(b, "Real:", b.real, "Imag:", b.imag)
print(c, "Real:", c.real, "Imag:", c.imag)

# 7. Boolean data type
x = True
y = False
print(x, type(x))
print(y, type(y))

# 8. Type casting
i = 10
f = 12.5
c = 3 + 4j

# int → float
print(float(i))
# float → int
print(int(f))
# int → complex
print(complex(i))
# complex → int (not allowed directly)
# print(int(c))   # ❌ Error
# complex → float (not allowed directly)
# print(float(c)) # ❌ Error
# float → complex
print(complex(f))