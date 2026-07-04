# What is the purpose of the type() function? Show its ouput for: type(10), type(10.5), type(True), type("hello")
print("Checking type(10):", type(10))
print("Checking type(10.5):", type(10.5))
print("Checking type(True):", type(True))
print("Checking type('hello'):", type("hello"))

#Explain operator precedence in Python. Evaluate the expression: 3 + 4 * 2 ** 2 - 1
calc = 3 + 4 * 2 ** 2 - 1
print(calc) #It followed the following order: -Raised to the power, -Multiplication, -Addition, & -Subtraction
# In the Equation 3 + 4 * 2 ** 2 - 1
# 2 ** 2 = 4 (Two raised to the power of 2 gives 4)
# 4 * 4 = 16 (4 from the equation, multiplied by 4 gotten from 2 ** 2, give 16)
# 3 + 16 = 19 (3 from the equation plus the 16 gotten from above, gives 19)
# 19 - 1 = 18 (19 gotten also for the equation above minus 1 from the equation, give 18)

#What is the difference between break and continue statements? Write program segment:
#For a loop that prints numbers from 1 to 10 but skips 5 using continue.
for i in range(1, 10):
    if i == 5:
        continue #From the output, this checks if in range 1 to 10, there exist 5, if True, then it generates till 10
    print(i)
print()

#And also for a loop that stops at 5 using break
for i in range(1, 10):
    if i == 5:
        break #From the output, this checks if in range 1 to 10, there exist 5, if True, then it stops generating
    print(i)
print()