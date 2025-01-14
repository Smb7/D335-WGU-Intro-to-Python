#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

# it's asking for input of times a employee drove to work 
# so get input (times x went to work) then * that by distance (miles)
EmpA = int(input())
DistA = float(15.62)
EmpA_Total = DistA * EmpA

EmpB = int(input())
DistB = float(41.85)
EmpB_Total = DistB * EmpB

EmpC = int(input())
DistC = float(32.67)
EmpC_Total = DistC * EmpC

total = EmpA_Total + EmpB_Total + EmpC_Total

print(f"Distance: {total:.2f} miles")