# 33.13 LAB: Warm up: Text analyzer & modifier
# Only got 4/6, can't figure out the issue, will come back to at later time

def get_num_of_characters(input_str):
    lengthstr = len(input_str)  # Get the length of the string
    strippedstr = input_str.replace(" ", "",)  # Remove spaces

    # Construct the output with the exact formatting
    output = (
        f"\nYou entered: {input_str}\n\n"
        f"Number of characters: {lengthstr}\n"
        f"String with no whitespace: {strippedstr}"
    )
    return output


if __name__ == '__main__':
    print("Enter a sentence or phrase:")
    input_str = input()  # User enters input on the next line
    print(get_num_of_characters(input_str))
