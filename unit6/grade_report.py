# Unit 6 Practical Task: Grade Report Generator

# Task Overview
# Extend the Unit 5 grade classifier into a full grade report generator called grade_report.py.
# The program must process a list of student dictionaries (each with name and marks for three subjects),
# generate a grade and status for each student, and produce a full class summary report.

# Requirements

# • Store at least 5 students as a list of dictionaries: [{name, maths, english, science}, …]
# • Use a for loop to iterate over all students and calculate each student’s average
# • Apply the grade/status logic from Unit 5 inside the loop
# • Build a results list of dictionaries containing: name, average, grade, status
# • After the main loop, calculate: class average, highest mark, lowest mark
# • Display a formatted class report showing individual results and class statistics
# • Use a while loop to let the user search for a student by name after the report is shown


# --- Store student data ---
students = [
    {"name": "Thabo", "maths": 78, "english": 65, "science": 82},
    {"name": "Naledi", "maths": 45, "english": 55, "science": 38},
    {"name": "Sipho", "maths": 90, "english": 88, "science": 95},
    {"name": "Zanele", "maths": 60, "english": 72, "science": 58},
    {"name": "Karabo", "maths": 33, "english": 40, "science": 47},
]

results = []

# --- Process each student ---
for student in students:
    average = round((student["maths"] + student["english"] + student["science"]) / 3, 2)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

# --- Class statistics ---
all_averages = []
for result in results:
    all_averages.append(result["average"])

class_average = round(sum(all_averages) / len(all_averages), 2)
highest_mark = max(all_averages)
lowest_mark = min(all_averages)

# --- Display the class report ---
print("\n--- Class Grade Report ---")
for result in results:
    print(f"{result['name']:<10} Average: {result['average']:<7} Grade: {result['grade']:<3} Status: {result['status']}")

print("\n--- Class Statistics ---")
print(f"Class Average: {class_average}")
print(f"Highest Average: {highest_mark}")
print(f"Lowest Average: {lowest_mark}")

# --- Student lookup ---
while True:
    search_name = input("\nEnter a student name to search (or 'exit' to quit): ").strip().lower()

    if search_name == "exit":
        print("Goodbye!")
        break

    found = False
    for result in results:
        if result["name"].lower() == search_name:
            print(f"Name: {result['name']}")
            print(f"Average: {result['average']}")
            print(f"Grade: {result['grade']}")
            print(f"Status: {result['status']}")
            found = True
            break

    if not found:
        print("Student not found.")