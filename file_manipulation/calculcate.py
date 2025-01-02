print("Reading in data...")
f = open('data.txt')
lines = f.readlines()
f.close()

print("\nCalculating average...")
total = 0 
for ln in lines:
    total += int(ln)

# computer result
avg = total/len(lines)
print(f"Average values: {avg:.2f}")