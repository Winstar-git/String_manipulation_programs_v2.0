# Prog01. lstrip() remove the space characters at the beginning of the string. 
# Create a program that do the same functionality without using lstrip() function.

# Define a function remove_leading_spaces that takes a string as input.
def remove_leading_space(text):
# Initialize an count_space variable to 0.
    count_space = 0
# Loop while the index is within the string length and the current character is a space.
    while count_space <= len(text) and text[count_space] == " ":
#     Increment the index.
        count_space += 1
# Return the substring starting from the first non-space character.
    return text[count_space:]

print(remove_leading_space(input("Enter a text with leading spaces: ")))