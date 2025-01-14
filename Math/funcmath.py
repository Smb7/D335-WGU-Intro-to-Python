import math

def calculation(x, y, z):
    # x power z
    value1 = math.pow(x, z)
    
    # x to power of (y power z)
    ypow = math.pow(y, z)
    value2 = math.pow(x, ypow)
    
    # absolute value of x - y
    value3 = x - y
    
    # square root x power y
    value4 = math.sqrt(value1)
    
    print(f"{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}")

x = float(input())
y = float(input())
z = float(input())

calculation(x,y,z)