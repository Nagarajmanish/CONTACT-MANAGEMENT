import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new contact
def add_contact(name, phone, email):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)''', (name, phone, email))
    conn.commit()
    conn.close()

# Function to view all contacts
def view_contacts():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    rows = c.fetchall()
    conn.close()
    return rows

# Function to update a contact
def update_contact(id, name, phone, email):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''UPDATE contacts SET name=?, phone=?, email=? WHERE id=?''', (name, phone, email, id))
    conn.commit()
    conn.close()

# Function to delete a contact
def delete_contact(id):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''DELETE FROM contacts WHERE id=?''', (id,))
    conn.commit()
    conn.close()

# Main function
if _name_ == "_main_":
    create_table()
    while True:
        print("\nAddress Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
            print("Contact added successfully!")
        elif choice == '2':
            contacts = view_contacts()
            if contacts:
                print("\nContacts:")
                for contact in contacts:
                    print(contact)
            else:
                print("No contacts found.")
        elif choice == '3':
            id = input("Enter ID of contact to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            update_contact(id, name, phone, email)
            print("Contact updated successfully!")
        elif choice == '4':
            id = input("Enter ID of contact to delete: ")
            delete_contact(id)
            print("Contact deleted successfully!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
