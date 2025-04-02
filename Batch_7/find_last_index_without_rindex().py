# Prog10. rindex() returns the first location of the function parameter in the string starting from the last character. 
# Create a program that does the same functionality without using rindex() function.

# Define a function find_last_index that takes a string and a character as input.
def find_last_index(text, char):
# Loop through each character in the string in reverse order.
    for chr in range(len(text) - 1, -1, -1):
#     If the character matches the input character, return the index.
        if text[chr] == char:
            return chr
# Return -1 if the character is not found.
    return -1

txt = str(input("Enter a text: "))
ch = str(input("Enter a character: "))
print(find_last_index(txt, ch))
