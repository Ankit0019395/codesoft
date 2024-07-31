class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"Contact {index}:")
                print(contact)

    def search_contacts(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        
        if not found_contacts:
            print("No contacts found.")
        else:
            print(f"Found {len(found_contacts)} contact(s):")
            for contact in found_contacts:
                print(contact)

    def update_contact(self, search_term):
        found_contacts = []
        for index, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append((index, contact))
        
        if not found_contacts:
            print("Contact not found.")
        else:
            print(f"Found {len(found_contacts)} contact(s):")
            for index, contact in found_contacts:
                print(f"Contact {index + 1}:")
                print(contact)
            
            contact_index = int(input("Enter the number of the contact to update: ")) - 1
            contact = self.contacts[contact_index]

            print("\nEnter new details (leave blank to keep existing):")
            new_name = input(f"Name ({contact.name}): ").strip() or contact.name
            new_phone_number = input(f"Phone ({contact.phone_number}): ").strip() or contact.phone_number
            new_email = input(f"Email ({contact.email}): ").strip() or contact.email
            new_address = input(f"Address ({contact.address}): ").strip() or contact.address

            updated_contact = Contact(new_name, new_phone_number, new_email, new_address)
            self.contacts[contact_index] = updated_contact
            print(f"\nContact '{contact.name}' updated successfully.\n")

    def delete_contact(self, search_term):
        found_contacts = []
        for index, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append((index, contact))
        
        if not found_contacts:
            print("Contact not found.")
        else:
            print(f"Found {len(found_contacts)} contact(s):")
            for index, contact in found_contacts:
                print(f"Contact {index + 1}:")
                print(contact)
            
            contact_index = int(input("Enter the number of the contact to delete: ")) - 1
            contact = self.contacts.pop(contact_index)
            print(f"\nContact '{contact.name}' deleted successfully.\n")

def main():
    contact_list = ContactList()

    while True:
        print("\nWelcome to the Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit\n")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nAdd Contact:")
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_list.add_contact(new_contact)

        elif choice == '2':
            print("\nView Contacts:")
            contact_list.view_contacts()

        elif choice == '3':
            print("\nSearch Contacts:")
            search_term = input("Enter name or phone number to search: ")
            contact_list.search_contacts(search_term)

        elif choice == '4':
            print("\nUpdate Contact:")
            search_term = input("Enter name or phone number to update: ")
            contact_list.update_contact(search_term)

        elif choice == '5':
            print("\nDelete Contact:")
            search_term = input("Enter name or phone number to delete: ")
            contact_list.delete_contact(search_term)

        elif choice == '6':
            print("\nThank you for using the Contact Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
