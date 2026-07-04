#Explain the term “function” in Python
#A function is a named, resuable block of code that performs a specific task. It accepts parameters (Inputs),
#Processes them, and returns an output. Functions let us avoid repeating code and make programs easier to read,
#test, and maintain. It can also be user-defined, or in-built. It can be imported to avoid bulky code and for code
# readability and usability. EXAMPLE OF A FUNCTION BELOW:
def greet_user(name): #The function is for greeting every user and accepts (name) as the parameter
    return f"Hello, {name} Welcome to Fuoye" #This is the condition or the instruction given for every name inputted
print(greet_user("Choco")) #This accepts the parament and print the instruction

#Explain string slicing with the syntax: [start:stop:step]
#String slicing is used to manipulate strings.
# - Start: This the index to begin the slicing from (The beginning value is defaultly 0)
# - Stop: This is the index to end the slicing at
# - Step:   This is to set how many characters to move each time. Negative steps moves backwards throught the string

#) Given:  s = "Python Programming" Write slices to obtain: - "Python", - "Programming", - Every second character,
# The string in reverse
str_value = "Python Programming"
print("First word:", str_value[0:6])
print("Second word:", str_value[7:19])
print("Every Second Character:", str_value[::2])
print("The String in Reverse:", str_value[::-1])

# Write a program segment of your choice to demonstrate the use of import math (math.pi)
import math
def circle_area(radius):
    return math.pi * radius ** 2
r = 5
print(f"math.pi = {math.pi}")
print(f"Area of a circle with radius {r}: {circle_area(r)}")