# QUESTION 2A: PROGRAM TO READ A TEXT FILE, COUNT THE NUMBER OF WORDS, AND WRITE THE RESULT TO ANOTHER FILE.
def count_words_in_file(input_path, output_path):
    try:
        with open(input_path, "r") as infile:
            content = infile.read()
            word_count = len((content.split()))

        with open(output_path, "w") as outfile:
            outfile.write(f"word count for '{input_path}': {word_count}\n")

        print(f"Success: {word_count} words found, Result written to {output_path}") 
    
        # PROGRAM WITH EXCEPTION HANDLING FOR MISSING FILE 
    except FileNotFoundError:
       print(f"Error: The file '{input_path}' does not exist")
    except Exception as e: 
       print(f"An unexpected error occured: {e}")

with open("sample_input.txt", "w") as f:
     f.write("i am from imo state")
count_words_in_file("sample_input.txt", "word_count_result.txt")
count_words_in_file("this_file_does_not_exist", "word_count_result.txt")

# IMPLEMENTING A CLASS STUDENT WITH ATTRIBUTES (NAME, ROLL NUMBER, MARKS) AND METHODS TO CALCULATE GRADE
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def grade_calculation(self):
        if self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 45:
            return "D"
        elif self.marks >= 40:
            return "E"
        else:
            return "F"
        
    def display(self):
        print(f"Name: {self.name} | Roll Number: {self.roll_number} | Marks: {self.marks} | Grade: {self.grade_calculation()}")

#  2C Extend the class with inheritance to create a subclass GraduateStudent with additional attributes (resarch_topic).       
class GraduateStudent(Student):
    def __init__(self, name, roll_number, marks, research_topic):
        super(). __init__(name, roll_number, marks) 
        self.research_topic = research_topic

    def display(self):
        super().display()
        print(f"Research Topic: {self.research_topic}")

stud_details = Student("Naomi", "DSA/2024/1066", 82) 
stud_details.display() 

grad_details = GraduateStudent("Divine", "CSC/2024/1128", 75, "Data Analytics") 
grad_details.display()