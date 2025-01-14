#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
def get_dist_total(usrinput):
    tons = (usrinput // 16) // (2000)
    print(f"Tons: {tons}")
    
    pounds = (usrinput // 16) % (2000)
    print(f"Pounds: {pounds}")
    
    ounces = (usrinput % 16)
    print(f"Ounces: {ounces}")
    
usrinput = int(input())
get_dist_total(usrinput)