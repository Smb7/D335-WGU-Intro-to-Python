import math

# this was an answer I could not answer on the test. 
def check(num):
    if num < 0:
        False
    sqrt = math.sqrt(num)
    print(f"{sqrt:.2f}")
    return sqrt.is_integer()

def numcheck(num):
    sqrt = math.sqrt(num)
    boolcheck = sqrt.is_integer()
    if boolcheck == True:
        print(f"{sqrt:.2f}")
        print(boolcheck)
    else:
        print(f"{sqrt:.2f}")
        print(False)

#print(check(81))
#print(check(35))


numcheck(36)
numcheck(35)