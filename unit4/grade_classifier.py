# Unit 4 Practical Task: Student Grade Classifier
# Task Overview

# Build a student grade classifier called grade_classifier.py that takes a learner’s
# name and marks for three subjects, calculates an average, assigns a grade and a status
# (Pass/Fail), and displays a full report card. The program must correctly use conditionals
# for all grade and status logic.

# Requirements

# Collect learner name and marks for three subjects (as floats) using input()
# Calculate the average mark across the three subjects
# Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
# Assign Pass status if the average is 50 or above, Fail otherwise
# Flag any individual subject mark below 40 as ‘needs intervention’
# Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags


# --- Collect input ---
name = input("Enter learner's name: ")
subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

# --- Calculate average ---
average = round((subject1 + subject2 + subject3) / 3, 2)

# --- Assign letter grade ---
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

# --- Assign pass/fail status ---
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# --- Check for intervention flags ---
subjects = {
    "Subject 1": subject1,
    "Subject 2": subject2,
    "Subject 3": subject3
}

intervention_flags = []
for subject_name, mark in subjects.items():
    if mark < 40:
        intervention_flags.append(subject_name)

# --- Display report card ---
print(f"\n--- Report Card for {name.title()} ---")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Average:   {average}")
print(f"Grade:     {grade}")
print(f"Status:    {status}")

if intervention_flags:
    print(f"Needs Intervention: {', '.join(intervention_flags)}")
else:
    print("Needs Intervention: None")