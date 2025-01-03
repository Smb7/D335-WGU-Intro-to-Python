# Question 7
"""
Input:
7
15
3

Output:
3

"""

int1 = int(input())
int2 = int(input())
int3 = int(input())

def check(int1, int2, int3):
    mylist = []
    mylist.append(int1)
    mylist.append(int2)
    mylist.append(int3)
    
    # find lowest value
    minval = min(mylist)
    print(minval)
    
check(int1, int2, int3)