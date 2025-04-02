# Prog05. startswith() checks if the string begins with a given prefix. 
# Create a program that does the same functionality without using startswith() function.

# Define a function starts_with that takes a string and a prefix as input.
def starts_with(text, prefix):
# If the prefix length is greater than the string length, return False.
    if len(prefix) > len(text):
        return False
# Compare the beginning characters of the string with the prefix.
    for char in range(len(prefix)):
#     If they match, return True.
        if text[char] == prefix[char]:
            return True
#     Otherwise, return False.
        else:
            return False
txt = str(input("Enter a text: "))        
pref = str(input("Enter prefix: "))
print(starts_with(txt, pref))