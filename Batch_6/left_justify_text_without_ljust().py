# Prog06. ljust() adds space characters at the end of the string to complete the specified number of characters. 
# Create a program that does the same functionality without using ljust() function.

# Define a function left_justify that takes a string and width as input.
def left_justify(text, width):
# If the string length is less than width:
    if len(text) < width:
#     Add spaces to the right until the width is reached.
        right_space = text + " " * (width - len(text))
# Return the modified string.
        return right_space
    else:
        return text
    
txt = str(input(" Enter text: "))
wdt = int(input("Enter width: "))

print(left_justify(txt, wdt))