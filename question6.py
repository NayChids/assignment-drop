# Use Pandas string methods to convert names to lowercase and get the domain from each email address.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["David Paul", "Aisha Bello", "Samuel Okoro", "Esther James", "Michael Ade",
         "Joy Nwosu", "Daniel Yusuf", "Mercy Ani", "Kelvin Ojo", "Ruth Simon"],

"email": ["david.paul@gmail.com", "aisha.bello@yahoo.com", "samuel.okoro@school.edu.ng",
          "esther.james@gmail.com", "michael.ade@outlook.com", "joy.nwosu@yahoo.com",
          "daniel.yusuf@school.edu.ng", "mercy.ani@gmail.com", "kelvin.ojo@outlook.com",
          "ruth.simon@gmail.com"],

"month": ["Feb", "Apr", "Jun", "Aug", "Oct", "Dec", "Jan", "Mar", "May", "Jul"],

"marks": [74, 68, 81, 59, 93, 77, 64, 88, 71, 85],

"math_score": [78, 70, 85, 62, 95, 80, 68, 90, 75, 87],

"science_score": [72, 69, 83, 60, 91, 79, 66, 86, 73, 84],
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print(df)

# Convert all names to lowercase
df["name_lower"] = df["name"].str.lower()
print(df[["name", "name_lower"]])

# Get domain names from email addresses
df["email_domain"] = df["email"].str.split("@").str[1]
print(df[["email", "email_domain"]])

# Plot a line chart of students' performance across months.
plt.figure(figsize=(8, 5))
plt.plot(df["month"], df["marks"], marker="o", color="tab:blue")
plt.title("Student Performance Across Months")
plt.xlabel("Month of the Year")
plt.ylabel("Marks Obtained")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("student_marks_trend.png", dpi=150)
plt.close()
print("\nChart saved as: student_marks_trend.png")

# Plot: Histogram showing the spread of students' marks
plt.figure(figsize=(8, 5))
plt.hist(df["marks"], bins=6, color="tab:orange", edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("student_marks_distribution.png", dpi=150)
plt.close()

print("Chart saved as: student_marks_distribution.png")

# Plot: Scatter chart comparing Mathematics and Science scores
plt.figure(figsize=(8, 5))
plt.scatter(df["math_score"], df["science_score"], color="tab:green")
plt.title("Comparison of Mathematics and Science Scores")
plt.xlabel("Mathematics Score")
plt.ylabel("Science Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("math_science_comparison.png", dpi=150)
plt.close()

print("Chart saved as: math_science_comparison.png")