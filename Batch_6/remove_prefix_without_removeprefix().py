# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.

# Define a function remove_prefix that takes a string and a prefix as input.
def remove_prefix(text, prefix):
# Check if the string starts with the prefix.
    if text.startswith(prefix):
#     If true, return the substring after the prefix.
        return text[len(prefix):]
#     Otherwise, return the original string.
    return text

txt = str(input("Enter a text: "))
pref = str(input("Enter prefix: "))

print(remove_prefix(txt, pref))
