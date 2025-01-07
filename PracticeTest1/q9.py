"""

Input:
-15
10

Output:
-15 -10 -5 0 5 10 

"""

int1 = -15
int2 = 10

if int1 <= int2:
    while int1 <= int2:
        print(int1, end=' ')
        int1 += 5
    print()
else:
    print("Second integer can't be less than the first.")