#############################################
"""SIMPLE CONTACT MANAGER
Write a Python program that:
- Prompts the user to input contact names and phone numbers
- Stores each contact as a name-number pair
- Saves the list to a text file when the user finishes entering contacts
If the user enters “done” the program ends and saves the data in a contacts.txt file which looks like the following:
"""
#############################################

def contact_manager() :
    # Simple Contact List Manager with List

    contacts : list = []

    while True:
        # Prompt for contact name
        name = input("Enter contact name (or type 'done' to finish): ").strip()

        if name.lower() == 'done':
            break

        # Prompt for contact phone number
        phone_number = input(f"Enter phone number for {name}: ").strip()

        # Add the contact to the list
        contacts.append(f"{name}: {phone_number}")

    # Write the contacts to a text file
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(contact + "\n")

    print("Contacts saved to 'contacts.txt'.")

# contact_manager()

def contact_manager_2() :
# Alternative Solution with dictionary use
    contacts : dict = {}

    while True :
        initial_input: str = input("Enter contact name (or type 'done' to finish): ").strip()

        match initial_input :
            case 'done':
                with open("contact_manager_challenge/contacts.txt", "w") as file :
                    for name, phone_number in contacts.items():
                        file.write(f'{name}: {phone_number}\n')
                print("Your contacts.txt has been saved")
                break
            case _:
                phone : str = input(f"Enter {initial_input}'s phone number: ")
                # Add the duo name-phone into the dictionary
                contacts[initial_input] = phone

# contact_manager_2()