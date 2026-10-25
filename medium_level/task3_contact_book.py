"""
Medium Level - Task 3: Contact Book Program
Objective: Store and manage data using a Python dictionary.

A menu-driven contact management system that supports
adding, viewing, and searching contacts.
"""

contacts = {}  # {name: {"phone": ..., "email": ...}}


def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print(f"A contact named '{name}' already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")


def view_contacts():
    if not contacts:
        print("\nNo contacts saved yet.")
        return
    print(f"\n{'Name':<20}{'Phone':<15}{'Email':<30}")
    print("-" * 65)
    for name, details in contacts.items():
        print(f"{name:<20}{details['phone']:<15}{details['email']:<30}")


def search_contact():
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"\nContact found!")
        print(f"Name  : {name}")
        print(f"Phone : {details['phone']}")
        print(f"Email : {details['email']}")
    else:
        print(f"\nNo contact found with the name '{name}'.")


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye! Your contacts are saved for this session.")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


main()
