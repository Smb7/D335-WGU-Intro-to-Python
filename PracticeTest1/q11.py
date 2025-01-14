"""
Input: 
7

Output:
fibonacci(7) is 13
"""
def fibonacci(n):
    if n < 0: # if less then 1 it return -1 
        return -1
    elif n == 0: # if equal to 1 it returns 1 
        return 0
    elif n == 1 or n == 2: # if n equals 1 or 2 it will return 1 
        return 1
    else:
        a, b = 1, 1
        for x in range(3, n + 1):
            a, b = b, a + b
        return b

start_num = int(input())
print(f'fibonacci({start_num}) is {fibonacci(start_num)}')

