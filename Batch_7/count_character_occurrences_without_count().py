# Prog08. count() returns how many times the function parameter appears in the string. 
# Create a program that does the same functionality without using count() function.

# Define a function count_occurrences that takes a string and a character as input.
def count_occurrence(text, char):
# Initialize a counter variable to 0.
    count = 0
# Loop through each character in the string.
    for chr in text:
#     If the character matches the input character, increment the counter.
        if chr == char:
            count += 1
# Return the counter value.
    return count

txt = str(input("Enter a text: "))
ch = str(input("Enter a character: "))
print(count_occurrence(txt, ch))