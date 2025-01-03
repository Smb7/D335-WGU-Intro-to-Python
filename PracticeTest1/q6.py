"""
Input:
8005551212

Output:
(800) 555-1212
"""

phone_number = int(input())

strphone = str(phone_number)

# 800 555 1212
# 123 456 78910

p1 = strphone[0:3]
p2 = strphone[3:6]
p3 = strphone[6::]
print(f"({p1}) {p2}-{p3}")