# Unit 1 Practical Task: Student Info Formatter

# Write a Python script called student_info.py that collects personal information from the user
# and displays it in a formatted profile card. The program must demonstrate correct use of all
# four data types, string manipulation, arithmetic, and the f-string output format.

# Requirements
# Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float)
# Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’
# Display the name in UPPERCASE using .upper() and in Title Case using .title()
# Calculate and display the age in months (age × 12)
# Round the favourite number to 2 decimal places using round()
# Print the data type of each collected value using type()

# --- Collect input ---
first_name = input("Enter your first name: ")
surname = input("Enter your last surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# --- Build full name and greeting ---
full_name = f'{first_name} {surname}'
print(f"\nWelcome, {full_name}!\n")

# --- String manipulation ---
print(f'UPPERCASE: {full_name.upper()}')
print(f"Title Case: {full_name.title()}")

# --- Arithmetic ---
age_in_months = age * 12
print(f"Age in months: {age_in_months}")

# --- Rounding ---
rounded_favourite = round(favourite_number, 2)
print(f'Favourite number (rounded to 2 decimals): {rounded_favourite}')

# --- Data types ---
print("\n--- Data Types ---")
print(f"first_name is of type: {type(first_name)}")
print(f"surname is of type: {type(surname)}")
print(f"age is of type: {type(age)}")
print(f"favourite number is of type: {type(favourite_number)}")

# --- Bonus --- Boolean type ---
is_student = True
print(f"is_student is of type: {type(is_student)}")








