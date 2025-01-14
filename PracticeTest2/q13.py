import csv

# Step 0: Get the input filename from the user
filename = input().strip()  # Remove any extra whitespace from the filename input

# Step 1: Read the file and process its contents
with open(filename, 'r') as file:
    reader = csv.reader(file)
    rows = [list(map(str.strip, row)) for row in reader]  # Strip whitespace from each value

# Step 2: Convert rows into dictionaries
dict1 = {key.strip(): value.strip() for key, value in zip(rows[0][::2], rows[0][1::2])}
dict2 = {key.strip(): value.strip() for key, value in zip(rows[1][::2], rows[1][1::2])}

# Step 3: Print the dictionaries in the required format
print(dict1)
print(dict2)