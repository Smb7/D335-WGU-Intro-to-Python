# going over indexing within a list

# practice #1 

"""
Obective:
Write a Python program that takes a list of numbers as input and prints the third element of the list. If the list has fewer than three elements, print "Not enough elements".

Ex1 input: 
numbers = [10, 20, 30, 40, 50]

output: 
The third element is: 30

input:
numbers = [5, 15]

output:
Not enough elements

"""

amount_of_inputs = int(input("Enter amount of times you would like to input a number: "))
x = 0 

while amount_of_inputs != x:
    numbers = []

    insert_number = int(input("Enter number to be inputed: "))
    x += 1

for num in enumerate(numbers):
    if num == 3:
        print(num)
    else:
        print("Not enough elements")

