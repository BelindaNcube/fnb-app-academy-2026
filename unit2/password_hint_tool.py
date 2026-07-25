# Unit 2 Challenge: The Secure Password Hint Tool

# Users often forget their passwords. Create a script that helps them by showing a secure hint.

# 1. Ask the user to input their secret password.
# 2. Use .strip() to clean up any accidental spaces they might have typed at the start or end.
# 3. Grab the very first letter and the very last letter of the password using string indexing.
# 4. Print a hint using an f-string that forces the letters into uppercase so they stand out.
# (e.g., “Your password hint: It starts with P and ends with N”).

password = input("Enter your secret password: ")

# --- Clean up whitespace ---
clean_password = password.strip()

# --- Grab first and last letter ---
first_letter = clean_password[0]
last_letter = clean_password[-1]

# --- Print the hint ---
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")