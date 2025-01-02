frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# Input CherryPy
# Expected output: Index: 2

usrinput = 'rocketman'

try:
    for index, item in enumerate(frameworks):
        if usrinput == item:
            print(f"Index: {index}")
except ValueError:
    print(f"Error")