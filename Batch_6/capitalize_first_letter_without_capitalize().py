# Prog09. capitalize() makes the first letter of the string uppercase and all other letters lowercase. 
# Create a program that does the same functionality without using capitalize() function.

# Define a function capitalize_first that takes a string as input.
def capitalize_first(text):
# If the string is empty, return it as is.
    if not text:
        return text
# Convert the first character to uppercase if it's a lowercase letter.
# Convert the rest of the string to lowercase.
# Return the modified string.
    if 'a' <= text[0] <= 'z':
        return text[0].upper() + text[1:].lower()
    else:
        return text[0].upper() + text[1:].lower()
    
print(capitalize_first(input("Enter text: ")))
