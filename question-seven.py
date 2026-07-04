# a. Define a class called Undergraduate. Attributes: Full Name, Student ID, Department, Year of Study, CGPA.
#  Methods: show_details(), determine_grade().
 
class Undergraduate:
    def __init__(self, full_name, student_id, department, year_of_study, cgpa):
        self.full_name = full_name
        self.student_id = student_id
        self.department = department
        self.year_of_study = year_of_study
        self.cgpa = cgpa

    def determine_grade(self):
        if 4.50 <= self.cgpa <= 5.00:
            return "First Class"
        elif 3.50 <= self.cgpa <= 4.49:
            return "Second Class Upper"
        elif 2.40 <= self.cgpa <= 3.49:
            return "Second Class Lower"
        elif 1.50 <= self.cgpa <= 2.39:
            return "Third Class"
        else:
            return "Pass"

    def show_details(self):
        print(f"Full Name: {self.full_name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")
        print(f"Year of Study: {self.year_of_study}")
        print(f"CGPA: {self.cgpa}")
        print(f"Degree Classification: {self.determine_grade()}")

undergraduates = [
    Undergraduate("David Paul", "ENG/2024/1201", "Engineering", 200, 4.85),
    Undergraduate("Godfrey Naomi", "BUS/2024/1215", "Business Administration", 300, 4.20),
    Undergraduate("Samuel Okoro", "CSC/2024/1180", "Computer Science", 100, 3.12),
    Undergraduate("Esther James", "BIO/2024/1122", "Biological Sciences", 400, 2.30),
    Undergraduate("Michael Ade", "ACC/2024/1167", "Accounting", 200, 1.75)
]

for undergraduate in undergraduates:
    undergraduate.show_details()