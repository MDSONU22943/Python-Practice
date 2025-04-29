import json
import os

CONTACTS_FILE="contacts.json"
def load_contact():
  if os.path.exists(CONTACTS_FILE):
    try:
      with open(CONTACTS_FILE,"r") as file:
        return json.load(file)
    except json.JSONDecodeError:
      print("Warning: Corrupted contacts file. Starting with an empty contact list.")
      return {}

  else:
    return {}

def save_contacts(contacts):
  with open(CONTACTS_FILE,"w") as file:
    json.dump(contacts,file)

def is_valid_phone(phone):
  return phone.isdigit() and len(phone)==10

def contact_book():
  contacts=load_contact()
  while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice =="1":
      name=input("Enter the name: ")
      if not name:
        print("Name cannot be empty.")
        continue
      if  name in contacts:
        print(f"Contact {name} already exists.")
        continue
      phone=input("Enter the phone number: ")
      if not is_valid_phone(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        continue
      contacts[name]=phone
      save_contacts(contacts)
      print("Contact added successfully!")
    
    elif choice =="2":
      print("\n--- Contacts ---")
      if not contacts:
        print("No contacts found.")
      else:
        for name, phone in contacts.items():
          print(f"{name}: {phone}")
    

    elif choice == "3":
      search_name=input("Enter the name to search: ")

      if search_name in contacts:
        print(f"Phone number of {search_name}: {contacts[search_name]}")
      else:
        print(f"Contact {search_name} not found.")

    elif choice == "4":
      edit_name=input("Enter the name to edit: ")
      if edit_name in contacts:
        new_phone=input("Enter the new phone number: ")
        if not is_valid_phone(new_phone):
          print("Invalid phone number. Please enter a 10-digit number.")
          continue
        contacts[edit_name]=new_phone
        save_contacts(contacts)
        print(f"Contact {edit_name} updated successfully!")
      else:
        print(f"Contact {edit_name} not found.")

    elif choice == "5":
      delete_name=input("Enter the name to delete: ")
      if delete_name in contacts:
        del contacts[delete_name]
        save_contacts(contacts)
        print(f"Contact {delete_name} deleted successfully!")
      else:
        print(f"Contact {delete_name} not found.")

    elif choice == "6":
      print("Exiting the contact book. Goodbye!")
      break
    else:
      print("Invalid choice. Please select a valid option.")

if __name__=="__main__":
  contact_book()

    