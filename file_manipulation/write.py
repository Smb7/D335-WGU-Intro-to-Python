"""
f = open('myfile.txt', 'w')
f.write('Example string:\n test......')
f.close()

r = open('myfile.txt', 'r')
content = r.read()
#print(f"This is the content:\n {content}")
r.close()
"""

# when writing a file it must be a string, otherwise it will produce an error 
f = open('myfile.txt', 'w')
try:
    f.write("123")
    f.close()
    print("Successfully wrote to file!")

except TypeError as er:
    print(er)