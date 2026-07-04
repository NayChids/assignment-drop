#Use Pandas string functions to: Convert all names to lowercase, Extract domain names from email addresses.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["John Doe", "Mary Jane", "Tunde Bello", "Amaka Eze", "Sade Ali",
             "Chinwe Obi", "Femi King", "Grace Udo", "Ibrahim Musa", "Linda Eke"],
    "email": ["john.doe@gmail.com", "mary.jane@yahoo.com", "tunde.b@school.edu.ng",
              "amaka.eze@gmail.com", "sade.ali@outlook.com", "chinwe.obi@yahoo.com",
              "femi.king@school.edu.ng", "grace.udo@gmail.com", "ibrahim.m@outlook.com",
              "linda.eke@gmail.com"],
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
    "marks": [65, 70, 58, 80, 90, 55, 72, 60, 85, 78],
    "math_score": [70, 65, 60, 85, 92, 50, 75, 62, 88, 80],
    "science_score": [68, 72, 55, 82, 89, 58, 70, 65, 84, 76],
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print(df)

# Convert all names to lowercase
df["name_lower"] = df["name"].str.lower()
print(df[["name", "name_lower"]])

# Extract domain names from email addresses
df["email_domain"] = df["email"].str.split("@").str[1]
print(df[["email", "email_domain"]])

# Plot: Line plot of marks over time
plt.figure(figsize=(8, 5))
plt.plot(df["month"], df["marks"], marker="o", color="tab:blue")
plt.title("Student Marks Over Time")
plt.xlabel("Month")
plt.ylabel("Marks")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("line_plot_marks_over_time.png", dpi=150)
plt.close()
print("\nSaved: line_plot_marks_over_time.png")

# Plot: Histogram of marks distribution
plt.figure(figsize=(8, 5))
plt.hist(df["marks"], bins=6, color="tab:orange", edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_marks_distribution.png", dpi=150)
plt.close()
print("Saved: histogram_marks_distribution.png")

# Plot: Scatter plot: math vs science scores
plt.figure(figsize=(8, 5))
plt.scatter(df["math_score"], df["science_score"], color="tab:green")
plt.title("Math Score vs Science Score")
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scatter_math_vs_science.png", dpi=150)
plt.close()
print("Saved: scatter_math_vs_science.png")