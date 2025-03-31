# Prog10. title() makes the first letter of each word in the string uppercase, and all other letters lowercase. 
# Create a program that does the same functionality without using title() function.

# Define a function to_title_case that takes a string as input.
def title_case(text):
# Split the string into words.
    words = text.split()
    result = []
# Loop through each word.
    for word in words:
#     Apply capitalize_first function to each word.
        result.append(word.capitalize())
# Join the words back into a single string with spaces.
    result = " ".join(result)
# Return the modified string.
    return result

print(title_case(input("Enter a text: ")))