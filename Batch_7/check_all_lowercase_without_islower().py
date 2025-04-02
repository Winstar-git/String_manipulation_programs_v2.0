# Prog04. islower() checks if all characters of the string are in lowercase. 
# Create a program that does the same functionality without using islower() function.

# Define a function is_all_lowercase that takes a string as input.
def is_all_lower(text):
# Loop through each character in the string.
    for char in text:
#     If the character is uppercase ('A' to 'Z'), return False.
        if "A" <= char <= "Z":
            return "False"
# Return True if no uppercase letters are found.
    return "True"

print(is_all_lower(input("Enter a text to check if text is in lowercase: ")))
