def highest_occurrence_character(s):
    # holds character counts
    char_count = {}

    # Iterate of each character in given string
    for char in s:
        # If the character is not in the dictionary, initialize it
        if char not in char_count:
            char_count[char] = 0
        # Increment the count for the character
        char_count[char] += 1

    # Variables for highest occurrence character and its count
    high_char = None
    high_count = 0

    # to find the character with the highest count
    for char in char_count:
        if char_count[char] > high_count:
            high_count = char_count[char]
            high_char = char

    return high_char, high_count


# main
input_string = input("Enter a string: ")
character, count = highest_occurrence_character(input_string)
print(f"The maximally occuring character is '{character}' with a count of {count}.")