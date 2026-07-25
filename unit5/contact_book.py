# Unit 5 Practical Task: Command-Line Contact Book

# Task Overview

# Build a command-line contact book called contact_book.py that stores contacts as a list of
# dictionaries and allows the user to add, search, view, and delete contacts. This is a
# foundational data structure pattern used in virtually every real app.

# Requirements

# Store contacts as a list of dictionaries, each with keys: name, phone, email
# Implement an add_contact() function that appends a new dictionary to the list
# Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
# Implement a delete_contact(name) function that removes a contact by name
# Implement a view_all() function that displays all contacts in a formatted layout
# Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)
contacts = []


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully!\n")


def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted.\n")
            return
    print(f"No contact found with name '{name}'.\n")


def view_all():
    if not contacts:
        print("No contacts saved yet.\n")
        return

    print("\n--- All Contacts ---")
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 20)
    print()


# --- Menu loop ---
while True:
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_name = input("Enter name to search: ")
        result = search_contact(search_name)
        if result:
            print(f"Found: {result}\n")
        else:
            print("Contact not found.\n")
    elif choice == "3":
        delete_name = input("Enter name to delete: ")
        delete_contact(delete_name)
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-5.\n")