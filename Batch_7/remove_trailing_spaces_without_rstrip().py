# Prog01. rstrip() removes the space characters at the end of the string. 
# Create a program that does the same functionality without using rstrip() function.

# Define a function remove_trailing_spaces that takes a string as input.
def remove_trailing_spaces(text):
# Initialize a variable to the last character of the string.
    last_char = len(text) - 1
# Loop while the index is non-negative and the current character is a space.
    while last_char >= 0 and text[last_char] == " ":
#     Decrement the index.
        last_char -= 1
# Return the substring up to the last non-space character.
    return text[:last_char + 1]

print(remove_trailing_spaces(input("Enter text with trailing spaces: ")))
