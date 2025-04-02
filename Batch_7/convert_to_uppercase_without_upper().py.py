# Prog03. upper() converts all characters of the string into uppercase. 
# Create a program that does the same functionality without using upper() function.

# Define a function to_upper that takes a string as input.
def to_upper(text):
# Initialize an empty result string.
    result = ""
# Loop through each character in the string.
    for char in text:
#     If the character is lowercase ('a' to 'z'):
        if "a" <= char <= "z":
#       Convert it to uppercase by subtracting 32 from its ASCII value.
#       Append the character to the result.
            result += chr(ord(char)- 32)
        else:
            result += char
# Return the result.
    return result

print(to_upper(input("Enter a text: ")))
