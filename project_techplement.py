import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact with name '{name}' not found.")

def update_contact(contacts, name, phone=None, email=None):
    if name in contacts:
        if phone is not None:
            contacts[name]['phone'] = phone
        if email is not None:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact with name '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email address: ")
            add_contact(contacts, name, phone, email)

        elif choice == "2":
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)

        elif choice == "3":
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number (press enter to keep existing): ")
            email = input("Enter new email address (press enter to keep existing): ")
            update_contact(contacts, name, phone, email)

        elif choice == "4":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
