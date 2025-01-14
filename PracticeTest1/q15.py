# 33.15 LAB: Parsing dates
def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format

def check_date_format(user_string):
    try:
        sstr = user_string.split(" ", 3)
        monthstr = sstr[0]
        yearint = int(sstr[2])
        
        check_for = sstr[1].split(",")
        for i in check_for:
            if i == '':
                dayint = int(check_for[0])
                return dayint, monthstr, yearint

    except:
        return

try:
    returned_day, returned_month, yearint = check_date_format(user_string)  # Example input
    
    month_int = get_month_as_int(returned_month)
    
    # Print the returned values
    print(f"{month_int}/{returned_day}/{yearint}")

except:
    print()