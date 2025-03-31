# Prog07. center() adds space characters at the beginning and end of the string to print it at the center. 
# Create a program that does the same functionality without using center() function.

# Define a function center_text that takes a string and width as input.
def center_text(text, width):
# Compute the total padding needed.
    total_padding = max(0, width - len(text))
# Divide the padding evenly between left and right.
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
# Concatenate spaces, the string, and spaces.
    center = " " * left_padding + text + " " * right_padding
# Return the centered string.
    return center

txt = str(input("Enter a text: "))
wdt = int(input("Enter width: "))

print(center_text(txt, wdt))