total = int(input())

currancy = {'Dollar': 100, 'Quarter' : 25, 'Dime' : 10, 'Nickel' : 5, 'Penny' : 1}

# Flag to check if any change was processed
change_given = False

for key, value in currancy.items():
    if total >= value:  # Use >= to include cases where total equals the currency value
        currancy_value = total // value  # How many of this currency fit
        total -= currancy_value * value  # Subtract the total value of this currency
        
        # Handle singular and plural forms
        word = key
        if currancy_value > 1:
            if word.endswith("y"):
                word = word[:-1] + "ies"  # Change 'y' to 'ies' for plural
            else:
                word += "s"  # Add 's' for plural
        
        print(f"{currancy_value} {word}")
        change_given = True  # Set flag to True when any currency is processed

if not change_given:  # If no change was processed
    print("No change")
