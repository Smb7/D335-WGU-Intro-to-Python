"""
Input: 
4 
3
2
1

Output:
Amount: $1.41
"""
quarter_int = int(input())
quarter = quarter_int * 0.25

dime_int = int(input())
dime = dime_int * 0.10

nickel_int = int(input())
nickel = nickel_int * 0.05

pennie_int = int(input())
pennie = pennie_int * 0.01

total = quarter + dime + nickel + pennie 

print(f"Amount: ${total:.2f}")