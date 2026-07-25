# Unit 1 Challenge: The Concert Ticket Booker

# Create a program that acts as a digital ticket counter.

# 1. Ask the user for their name.
# 2. Ask them for the name of the band/artist they want to see.
# 3. Print a personalized confirmation message using an f-string that says
# something like: “Hey [Name]! Your tickets to see [Artist] are booked successfully!”

name = input("Enter your name: ").strip().title()
artist = input("Which band/artist do you want to see? ").strip().title()

print(f"Hey {name}! Your tickets to see {artist} are booked successfully!")