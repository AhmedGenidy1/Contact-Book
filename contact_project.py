#      Contact Book Project


contacts = {}  # Dictionary to store contacts


# ---------- Add Contact ----------
def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone: ").strip()

    if not name or not phone:
        print("Name or phone cannot be empty.")
        return

    if name in contacts:
        choice = input("Contact exists. Update number? (y/n): ").lower().strip()
        if choice == 'y':
            contacts[name] = phone
            print("Contact updated!")
        else:
            print("No changes made.")
    else:
        contacts[name] = phone
        print("Contact saved!")


# ---------- View All Contacts ----------
def view_contacts():
    if contacts:
        print("\n--- Contacts List ---")
        for i, (name, phone) in enumerate(contacts.items(), start=1):
            print(f"{i}. {name}: {phone}")
    else:
        print("No contacts found.")


# ---------- Search Contact ----------
def search_contact():
    name = input("Enter name to search: ").strip().title()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")


# ---------- Delete Contact ----------
def delete_contact():
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


# ---------- Update Phone ----------
def update_contact():
    name = input("Enter name to update phone: ").strip().title()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        if phone:
            contacts[name] = phone
            print("Phone updated.")
        else:
            print("Phone number cannot be empty.")
    else:
        print("Contact not found.")


# ---------- Update Name ----------
def update_name():
    old_name = input("Enter current name: ").strip().title()
    if old_name in contacts:
        new_name = input("Enter new name: ").strip().title()
        if new_name: 
            contacts[new_name] = contacts.pop(old_name)
            print(f"Name updated from {old_name} to {new_name}.")
        else:
            print("New name cannot be empty.")
    else:
        print("Contact not found.")


# ---------- Main Menu ----------
def main_menu():
    while True:
        print("\n==============================")
        print("        CONTACT BOOK")
        print("==============================")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Phone")
        print("6. Update Name")
        print("7. Exit")
        print("==============================")

        choice = input("Choice: ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            update_name()
        elif choice == '7':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
main_menu()

