various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

def find_data_type(usrinput):
    get_type = various_data_types[usrinput]
    converted_type = type(get_type).__name__
    print(f"Element {usrinput}: {converted_type}")


usrinput = int(input())
find_data_type(usrinput)