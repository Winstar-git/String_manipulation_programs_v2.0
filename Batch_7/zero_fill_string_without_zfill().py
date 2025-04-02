# Prog07. zfill() adds zero characters at the beginning of the string to reach a specified width. 
# Create a program that does the same functionality without using zfill() function.

# Define a function zero_fill that takes a string and width as input.
def zero_fill(text, width):
# If the string length is less than width:
    if len(text) < width:
#     Add '0' characters to the left until the width is reached.
        return "0" * (width -len(text)) + text
# Return the modified string.
    return text

txt = str(input("Enter a text: "))
wdt = int(input("Enter Width: "))
print(zero_fill(txt, wdt))
