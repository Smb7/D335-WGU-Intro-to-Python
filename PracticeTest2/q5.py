#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
#second output: sum of five inputs converted to float values
#third output: sum of five inputs converted to string values (concatenate)

ui1 = int(input())
ui2 = int(input())
ui3 = int(input())
ui4 = int(input())
ui5 = int(input())

UIsum = (ui1, ui2, ui3, ui4, ui5)

floatsum = (ui1, ui2, ui3, ui4, ui5)
convertToFloat = float(sum(UIsum))