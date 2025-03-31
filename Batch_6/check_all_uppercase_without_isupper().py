# Prog04. isupper() checks if all characters of the string are uppercase. 
# Create a program that does the same functionality without using isupper() function.

# Define a function is_all_uppercase that takes a string as input.
def is_all_uppercase(text):
# Loop through each character in the string.
    for char in text:
#     If the character is lowercase ('a' to 'z'), return False.
        if "a" <= char <= "z":
            return False
# Return True if no lowercase letters are found.
    return True

print(is_all_uppercase(input("Enter a text: ")))
