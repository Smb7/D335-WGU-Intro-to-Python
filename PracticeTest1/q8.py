# this is where I left off at 9:20pm on 1/2

usrinput = int(input())

dollar = 100
quarter = 25
dime = 10
nickel = 5
pennie = 1

def check(usrinput):
    check_dollar = usrinput // dollar
    print(check_dollar)
    
    check_quarter = usrinput // quarter
    print(check_quarter)
    
    check_dime = usrinput // dime
    print(check_dime)
    
    check_nickel = usrinput // nickel
    print(check_nickel)
    
    check_penny = usrinput // pennie
    print(check_penny)
    
    if check_dollar != 0:
        if check_dollar > 1:
            print(f"{check_dollar} Dollars")
        else:
            print(f"{check_dollar} Dollar")
    
    elif check_quarter != 0:
        if check_quarter == 1:
            print(f"{check_quarter} Quarter")
        else:
            print(f"{check_quarter} Quarters")
    
    elif check_dime != 0:
        if check_dime > 1:
            print(f"{check_dime} Dimes")
        else:
            print(f"{check_dime} Dime")
    
    elif check_nickel != 0:
        if check_nickel > 1:
            print(f"{check_nickel} Nickles")
        else:
            print(f"{check_nickel} Nickle")
    
    elif check_penny != 0:
        if check_penny > 1:
            print(f"{check_penny} Pennies")
        else:
            print(f"{check_penny} Penny")
    else:
        print("No change")