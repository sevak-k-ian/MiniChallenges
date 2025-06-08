#############################################
"""
CREATE A DAILY JOURNAL FOR MY THOUGHTS
A program that will create a txt file for everyday I want to write my mood/thoughts, to store the 
input of the user.
It will prompt like this :
Enters today's date : YYYY-MM-DD
Rate your mood from 1 to 10 : 
Write your thoughts of the day :
Optional features :
- prevent creating a daily journal for an already existing date
"""
#############################################

########################################
########## FUNCTIONS USED IN MAIN CODE
########################################
# Get command from user
def get_command_from_user() -> str :
    input_command: str = input("Write 'create', 'view journals' or 'exit': ")
    return input_command

# Get today date from user
def get_date_from_user() -> str :
    input_date : str = input("Enters today's date (format 'YYYY-MM-DD'): ")
    return input_date

# Get today mood rate from 1-10
def get_mood_from_user() -> str :
    input_mood : str = input("Rate your mood from 1 to 10 : ")
    return input_mood

# Get today's thoughts
def get_thoughts_from_user() -> str :
    input_thoughts: str = input("Write your thoughts of the day : " + "\n")
    return input_thoughts

# Explore all the existing txt journal
import os
def display_all_journals() -> None :
    files : list = os.listdir("journal_thoughts")
    sorted_files : list = sorted(files)
    print("Your list of current journals are:")
    [print(f'{journal}') for journal in sorted_files]

def find_duplicate_journal(date) -> bool :
    current_journals: list = os.listdir("journal_thoughts")
    current_filenames : list = [journal.replace(".txt","") for journal in current_journals]
    if current_filenames.count(f'{date}') > 0 :
        return True
    else :
        print(f'✅ We can continue your journal creation')

########################################
########## MAIN CODE / LOGIC OF THE APP
########################################
def daily_journal() -> None :
    while True :
        command : str = get_command_from_user()

        match command :
            case 'create':
                # Get today date from user
                date : str = get_date_from_user()

                # Check if there is already an existing journal with this date
                if find_duplicate_journal(date) :
                    print(f'⚠️ A journal for provided date ({date}) already exists. \n'
                          f"I can't accept your request.")
                else :
                    # Get the rest of data
                    mood : str = get_mood_from_user()
                    thoughts : str = get_thoughts_from_user()
                    # Write the collected data in a new file stored in the correct directory
                    with open(f'journal_thoughts/{date}.txt', 'w') as file:
                        file.write(f'Journal of {date}.\n')
                        file.write(f'My mood for the day is {mood}/10.\n')
                        file.write(f'My thoughts for the day are: \n{thoughts}')
                    # Aknowledge use about journal creation
                    print("✅ Your journal has been successfully created.")

            case 'view journals':
                display_all_journals()

            case 'exit':
                print(" 👋 Ok bye bye, see you soon")
                break

            case _:
                print("Unknown command")

daily_journal()

