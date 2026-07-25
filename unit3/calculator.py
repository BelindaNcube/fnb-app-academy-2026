# Unit 3 Practical Task: Multi-Function Calculator

# Multi-Function Calculator

# Build a Python calculator called calculator.py that takes two numbers as input and performs
# all four basic arithmetic operations plus two advanced operations. The calculator must
# handle user input safely using type casting and display results clearly using f-strings.

# Requirements

# Use float(input()) to collect two numbers from the user
# Calculate and display: addition, subtraction, multiplication, division
# Calculate and display: floor division (//) and modulus (%)
# Round all results to 2 decimal places using round()
# Handle division by zero — if the second number is 0, d

# --- Collect input ---
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"\n--- Results for {num1} and {num2} ---")

# --- Addition, subtraction, multiplication ---
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

print(f"Addition:       {num1} + {num2} = {addition}")
print(f"Subtraction:    {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")

# --- Division, floor division, modulus (guarded against zero) ---
if num2 == 0:
    print("Division:       Cannot divide by zero!")
    print("Floor Division: Cannot divide by zero!")
    print("Modulus:        Cannot divide by zero!")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"Division:       {num1} / {num2} = {division}")
    print(f"Floor Division: {num1} // {num2} = {floor_division}")
    print(f"Modulus:        {num1} % {num2} = {modulus}")

# --- Formatted summary table ---
print("\n--- Summary Table ---")
print(f"{'Operation':<15}{'Expression':<20}{'Result':<10}")
print("-" * 45)

print(f"{'Addition':<15}{f'{num1} + {num2}':<20}{addition:<10}")
print(f"{'Subtraction':<15}{f'{num1} - {num2}':<20}{subtraction:<10}")
print(f"{'Multiplication':<15}{f'{num1} * {num2}':<20}{multiplication:<10}")

if num2 == 0:
    print(f"{'Division':<15}{'N/A':<20}{'Cannot divide by 0':<10}")
    print(f"{'Floor Division':<15}{'N/A':<20}{'Cannot divide by 0':<10}")
    print(f"{'Modulus':<15}{'N/A':<20}{'Cannot divide by 0':<10}")
else:
    print(f"{'Division':<15}{f'{num1} / {num2}':<20}{division:<10}")
    print(f"{'Floor Division':<15}{f'{num1} // {num2}':<20}{floor_division:<10}")
    print(f"{'Modulus':<15}{f'{num1} % {num2}':<20}{modulus:<10}")