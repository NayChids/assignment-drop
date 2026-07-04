
# A function in Python is a named block of code that performs a specific task.
# It can take input (parameters), process the input, and return a result.
# Functions help reduce repeated code, make programs easier to read, test, and maintain.
# Python has built-in functions, and you can also create your own (user-defined) functions.
# Functions can also be imported from other files to keep code organized and reusable.
# Example of a function:

def greet_user(name): # This function greets every user by accepting their name as a parameter.
    return f"Hello, {name} Welcome to Fuoye" # This is the instruction that will be carried out for every name entered into the function.
print(greet_user("Nay")) # This accepts the parameter and prints the message based on the given instruction.

# Explain string slicing using the syntax: [start:stop:step]
# String slicing is used to extract or manipulate parts of a string.
# - Start: The index where slicing begins (default is 0).
# - Stop: The index where slicing ends (not included).
# - Step: The number of characters to move each time. A negative step slices the string backwards.

# Given:
# s = "Python Programming"

# Write slices to get:
# - "Python"
# - "Programming"
# - Every second character
# - The string in reverse
str_value = "Python Programming"
print("First word:", str_value[0:6])
print("Second word:", str_value[7:19])
print("Every Second Character:", str_value[::2])
print("The String in Reverse:", str_value[::-1])

# Write a program segment of your choice to demonstrate the use of import math (math.pi)
import math
def calculate_surface(size):
    return math.pi * size ** 2
value = 5
print(f"math.pi = {math.pi}")
print(f"The calculated value for size {value}: {calculate_surface(value)}")