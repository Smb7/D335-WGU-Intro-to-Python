#solution accepts three integer values representing base and height measurements of a trapezoid

#first and second integers represent base 1 and base 2; third integer represents height 

#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h
# A = [(b1 + b2) / 2] * h

b1 = int(input())

b2 = int(input())

height = int(input())

area = ((b1 + b2) / 2) * height

print(f"Trapezoid area: {area} square meters")

# another way I solved the problem
def calculate_area(b1, b2, h):
    a = ((b1 + b2) / 2) * h
    print(f"Trapezoid area: {a:.1f} square meters")

int1 = int(input())
int2 = int(input())
int3 = int(input())
calculate_area(int1, int2, int3)