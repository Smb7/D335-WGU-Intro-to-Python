# listing all my solutions and will test after I complete the practice exam 

# 1 question **I screwed up the formatting and have space on the edges**
empa = int(input())
empb = int(input())
empc = int(input())

total = (15.62 * empa) + (41.85 * empb) + (32.67 * empc)
print(f"Distance: {total:.2f} miles")

# 2 question ** Got correct
usrinput = int(input())

tons = (usrinput // 16) // 2000
pounds = (usrinput // 16) % 2000
ounces = (usrinput % 16)

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")

# 3 question ** Got correct
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

usrinput = int(input())

value = various_data_types[usrinput]
print(f"Element {usrinput}: {type(value).__name__}")

# 4 question ** Got correct
b1 = int(input())
b2 = int(input())
h = int(input())

a = ((b1 + b2) / 2) * h

print(f"Trapezoid area: {a} square meters")

#5 question **got correct 
int1 = int(input())
int2 = int(input())
int3 = int(input())
int4 = int(input())
int5 = int(input())

nums = [int1, int2, int3, int4, int5]

intsum = sum(nums)
floatsum = float(sum(nums))
stringnums = str(nums)

print(f"Integer: {intsum}")
print(f"Float: {floatsum}")
print(f"String: {int1}{int2}{int3}{int4}{int5}")

# 6 question ** Got correct
usrinput = int(input())

studentid = str(usrinput)

print(f"{studentid[0:3]}-{studentid[3:5]}-{studentid[5::]}")

# 7 question ** got correct 
predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list

value = int(input())
maxval = max(predef_list)

if value > maxval:
    print(f"Greater Than Max? True")

elif value <= maxval:
    print(f"Greater Than Max? False")

# 8 question **forgot to print caution hot... Otherwise it's 100%
temp = int(input())

if temp >= 212:
    print("Boiling")
    
elif temp == 212:
    "Caution: Hot!"
    
elif temp < 211 and temp >= 115:
    print(f"Hot")
    
elif temp < 115 and temp >= 80:
    print("Warm")
    
elif temp < 80 and temp >= 33:
    print("Cold")
    
elif temp < 33:
    print("Frozen")
    print("Watch out for ice!")

# 9 question **got correct 
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

index = int(input())

try:
    print(frameworks[index])
    
except:
    print("Error")

# 10 question **Got correct 
stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

stock_amount = int(input())

selected_stocks = []

x = 0 
while x != stock_amount:
    stock_selection = input()
    
    for stock, price in stocks.items():
        if stock == stock_selection:
            selected_stocks.append(price)
    x += 1


total = sum(selected_stocks)
print(f"Total price: ${total:.2f}")

# 11 question **got correct 
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

produce = input()
quanity = int(input())

for key, value in purchase.items():
    if key == produce:
        if quanity < 10:
            total = value * quanity
        
        elif quanity < 20 and quanity > 10:
            total = (value * quanity) * 0.95
        
        elif quanity >= 21:
            total = (value * quanity) * 0.90

print(f"{produce} ${total:.2f}")

# 12 question ** got corret 
filename = input()

f = open(filename, 'r')
lines = f.read()

formatted = " ".join(lines.split())
f.close()

a = open(filename, 'a')
a.write(f"\n{formatted}")
a.close()

f = open(filename, 'r')
lines = f.read()
print(lines)
f.close()

# 13 question 
import csv 

filename = input()

csvfile = open(filename, 'r')
csvread = csv.reader(csvfile)

dic1 = {}
dic2 = {}

for rows in csvread:
    print(rows)

# 14 question **got correct 
import math 

integer = int(input())

nums = math.factorial(integer)
if nums < 100:
    print(nums)
    print("False")

else:
    print(nums)
    print("True")

# 15 question ** got correct 
from pigAge import pigAge_converter

pig_age = int(input())

print(f"{pig_age} is {pigAge_converter(pig_age)} in human years")