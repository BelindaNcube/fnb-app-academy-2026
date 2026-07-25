# Unit 2 Practical Task: Username and Message Formatter

# Write a Python script called string_formatter.py that takes a user’s first name,
# last name, and a short bio message as input, then applies multiple string transformations to produce a
# formatted user profile output. This simulates how a real app backend processes user-submitted text.

# Requirements

# Collect first name, last name, and bio message using input()
# Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
# Display the full name in Title Case using .title()
# Strip leading/trailing whitespace from the bio before displaying it using .strip()
# Count and display the number of characters in the bio using len()
# Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
# Display all output using f-strings


# --- Collect input ---
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio message: ")

# --- Build username: first initial + last name, lowercase ---
username = f"{first_name[0].lower()}{last_name.lower()}"

# --- Full name in Title Case ---
full_name = f"{first_name} {last_name}".title()

# --- Clean the bio ---
clean_bio = bio.strip()

# --- Character count ---
bio_length = len(clean_bio)

# --- Replace 'I am' with 'I'm' ---
formatted_bio = clean_bio.replace("I am", "I'm")

# --- Output ---
print(f"\nUsername: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {formatted_bio}")
print(f"Bio character count: {bio_length}")
print(f"Position of 'bio' in the word 'biography': {'biography'.find('bio')}")
print(f"Bio split into words: {bio.split()}")