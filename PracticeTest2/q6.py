#hint: modulo (%) and floored division (//) may be used
#solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
#solution outputs formatted student identification number as a string (i.e.,"541-75-3010")

inputUsr = int(input())
ui = str(inputUsr)

if len(ui) == 9:
    str1 = ui[0:3]
    str2 = ui[3:5]
    str3 = ui[5::]
    result = str1 + "-" + str2 + "-" + str3
    print(result)