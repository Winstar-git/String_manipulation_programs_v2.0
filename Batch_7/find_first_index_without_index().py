# Prog09. index() returns the first location of the function parameter in the string. 
# Create a program that does the same functionality without using index() function.

# Define a function find_index that takes a string and a character as input.
def find_index(text, char):
# Loop through each character in the string with an index.
    for chr in range(len(text)):
#     If the character matches the input character, return the index.
        if text[chr] == char:
            return chr
# Return -1 if the character is not found.
    return -1

txt = str(input("Enter a text: "))
ch = str(input("Enter a character: "))
print(find_index(txt, ch))
