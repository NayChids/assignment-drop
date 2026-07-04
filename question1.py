# Create a code using the if-elif else conditional statement that classify student's score into grades 
def grade_function(grade):
    if grade >= 70:
        return "A"
    elif grade >= 60:
        return "B"
    elif grade >= 50:
        return "C"
    elif grade >= 45:
        return "D"
    elif grade >= 40:
        return "E"
    else:
        return "F"
    
# Writing the function that holds scores for five courses, calculates the average and grades it
def grade_summary(scores): #This line of code holds the courses scores
    average = sum(scores) / len(scores) #This line of code calculates the average
    avg_grade = grade_function(average) #This line of code gives the grade of the average

    print(f"Individual Scores: {scores}") #This is the code that generates the output of the Individual Scores
    print(f"Average Score: {average}") #This is the code that generates the output of the Average Score
    print(f"Grade: {avg_grade}") #This is the code that generates the output for the Average Grade
    return average, avg_grade

course_scores = [70, 87, 66, 100, 22] #This is where we assign the Scores for the five courses
grade_summary(course_scores) #This lets the scores undergo the calculations for average and grades


#QUESTION 1B: DEMONSTRATE THE USE OF LISTS, TUPLES, DICTIONARIES AND SETS WITH EXAMPLES
#Demonstrating the use of Lists with examples
my_List = ["Princess", "Divine", "Naomi", "Bethel"]
my_List.append("Collins")
print("Output for List", my_List)

#Demonstrating the use of Tuples with examples
my_Tuple = ("Pots", "Kettles", "Spoons")
print("Output for Tuple:", my_Tuple)

#Demonstrating the use of Dictionaries with examples
my_Dict = {
    "Name": "Naomi",
    "Course": "DTS 216",
    "Matric No.": "DSA/2024/1066"
}
print("Output for Dictionary:", my_Dict)
print("Assessing a specific data:", my_Dict["Course"])

#Demonstrating the use of Sets with examples
set_int = {55, 24, 43, 66, 78, 89}
print("Set:", set_int)


# QUESTION 1C: SHOW TYPE CONVERSION BETWEEN INT, FLOAT AND STRING
string_val = "72"
int_val = int(string_val)
float_val = float(int_val)
str_val = str(float_val)

print("Output for String to Int:", int_val, "Checking output type:", type(int_val))
print("Output for Int to Float:", float_val, "Checking output type:", type(float_val))
print("Output for Float back to string:", str_val, "Checking output type:", type(str_val))


#QUESTION 1D: IMPLEMENT A PROGRAM THAT USES LOOPS AND LOOP CONTROL STATEMENTS TO PRINT PRIME NUMBERS BETWEEN 1-100
for number in range(1, 100):
    is_prime = True

    for i in range(2, number):
        if number % i == 0: #This checks the number and divide each number by i(which means divides by 2 to 100) and if it has remainder then it is a prime number, else it is not
            is_prime = False
            break

    if is_prime:
        print(number)
