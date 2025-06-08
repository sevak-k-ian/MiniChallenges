# Write a Python script that:
# - Retrieves today’s date
# - Prompts the user to enter notes line by line
# - Stops input when the user types "exit"
# - Saves the content to a text file named YYYY-MM-DD.txt

# Retrieves today’s date
from datetime import datetime

now = datetime.now()  # current date and time
today: str = f"Today's date: {now.strftime("%A %d %B %Y")}"

# Saves the content to a text file named YYYY-MM-DD.txt
filepath: str = f"../save_daily_dates_notes_files/{now.strftime("%Y-%m-%d")}.txt"

# Prompts the user to enter notes line by line
print("Enter your today's note (to stop taking note your last line must be 'exit': \n")
exit_command: bool = True

notes: list = []
while exit_command:
    line_note: str = input("")
    if line_note == "exit":
        notes.insert(0, today + "\n\n")
        with open(filepath, "w") as file:
            file.writelines(notes)
        exit_command = False
        break
    else:
        notes.append(line_note + "\n")
