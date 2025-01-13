# 33.14 LAB: Palindrome

def check_for_palindrome(usrinput):
    stripped_input = usrinput.replace(" ", "",) # remove whitespace
    return stripped_input == stripped_input[::-1] 

usrinput = input()
ans = check_for_palindrome(usrinput)

if ans == True:
    print(f"{usrinput} is a palindrome")
elif ans == False:
    print(f"{usrinput} is not a palindrome")