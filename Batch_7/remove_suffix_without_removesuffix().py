# Prog02. removesuffix() removes the characters at the end of the string that match the function parameter. 
# Create a program that does the same functionality without using removesuffix() function.

# Define a function remove_suffix that takes a string and a suffix as input.
def remove_suffix(text, suffix):
# Check if the string ends with the suffix.
    if text[-len(suffix):] == suffix:
#     If true, return the substring excluding the suffix.
        return text[:-len(suffix)]
#     Otherwise, return the original string.
    return text
txt = str(input("Enter a text: "))
suff = str(input("Enter suffix: "))
print(remove_suffix(txt, suff))