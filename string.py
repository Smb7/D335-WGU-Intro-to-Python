# string slicing 
url = 'http://en.wikipedia.org/wiki/Turing'
domain = url[7:23]  # Read 'en.wikipedia.org' from url
print("string slicing")
print(f"7:23 --> {domain}")

domain = url[10:-6]
print(f"10:-6 --> {domain}")

domain = url[8::]
print(f"8:: --> {domain}")

domain = url[::23]
print(f"::23 --> {domain}")

print(f":-1 --> {url[:-1]}")

# Slice Stride
numbers = '0123456789'

print(f'All numbers: {numbers[::]}')
print(f'Every even number: {numbers[::2]}')
print(f'Every third number between 1 and 8: {numbers[1:9:3]}')
print(f'Every odd number between 1 and 9: {numbers[1:9:2]}')
