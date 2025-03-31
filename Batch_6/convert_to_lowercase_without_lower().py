# Prog03. lower() converts all characters of the string into lower case. 
# Create a program that do the same functionality without using lower() function.

# Define a function to_lowercase that takes a string as input.
def lowercase(text):
# Initialize an empty string for the result.
    result = ""
# Loop through each character in the string.
    for char in text:
#     If the character is uppercase ('A' to 'Z'):
        if "A" <= char <= "Z":
#         Convert it to lowercase by adding 32 to its ASCII value.
            result += chr(ord(char) + 32)
#     Append the character to the result.
        else:
            result += char
# Return the result.
    return result

print(lowercase(input("Enter a text: ")))