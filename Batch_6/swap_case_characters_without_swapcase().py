# Prog08. swapcase() reverses the casing of each character in the string. 
# Create a program that does the same functionality without using swapcase() function.

# Define a function swap_case that takes a string as input.
def swap_case(text):
# Initialize an empty result string.
    result = ""
# Loop through each character in the string.
    for char in text:
#     If the character is uppercase ('A' to 'Z'):
        if 'A' <= char <= 'Z':
#         Convert it to lowercase.
            result += chr(ord(char) + 32)
#     Else if the character is lowercase ('a' to 'z'):
        elif 'a' <= char <= 'z':
#         Convert it to uppercase.
            result += chr(ord(char) - 32)
#     Append the converted character to the result.
        else:
            result += char
# Return the result.
    return result

print(swap_case(input("Enter a text to swapcases: ")))
