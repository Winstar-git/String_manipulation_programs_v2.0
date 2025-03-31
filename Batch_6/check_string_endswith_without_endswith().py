# Prog05. endswith() checks if the string's end part matches the function parameter. 
# Create a program that does the same functionality without using endswith() function.

# Define a function ends_with that takes a string and a suffix as input.
def ends_with(text, suffix):
# If the suffix length is greater than the string length, return False.
    if len(suffix) > len(text):
        return False
# Compare the last characters of the string with the suffix.
    if text[-len(suffix):] == suffix:
#     If they match, return True.
        return True
#     Otherwise, return False.
    else:
        return False

txt = str(input("Enter a text: "))
suf = str(input("Enter suffix: "))
print(ends_with(txt, suf))