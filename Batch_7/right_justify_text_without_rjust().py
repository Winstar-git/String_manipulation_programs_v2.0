# Prog06. rjust() adds space characters at the beginning of the string to reach a specified width. 
# Create a program that does the same functionality without using rjust() function.

# Define a function right_justify that takes a string and width as input.
def right_justify(text, width):
# If the string length is less than width:
    if len(text) < width:
#     Add spaces to the left until the width is reached.
        return " " * (width - len(text)) + text
# Return the modified string.
    return text

txt = str(input("Enter a text: "))
wdt = int(input("Enter width: "))
print(right_justify(txt, wdt))