"""
Input:
Hello there
Hey
done

Output:
ereht olleH
yeH

"""

usrinput = input()

while True:
    if usrinput == 'Done' or usrinput == 'done' or usrinput == 'd':
        break
    else:
        print(usrinput[::-1])
        usrinput = input()
