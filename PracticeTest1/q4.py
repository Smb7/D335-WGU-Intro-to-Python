"""
Input:
20.0 miles
3.1599 cost per gallon

output:
3.16 11.85 79.00
"""

miles_int = float(input())
gas_int = float(input())

# 20 miles
miles20 = (20 / miles_int) * gas_int

# 75 miles 
miles75 = (75 / miles_int) * gas_int

# 500 miles
miles500 = (500 / miles_int) * gas_int
print(f"{miles20:.2f} {miles75:.2f} {miles500:.2f}")