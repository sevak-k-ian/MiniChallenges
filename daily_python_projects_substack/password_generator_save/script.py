###############################################
# EXTERNAL LIB AND MODULES
###############################################
from nicegui import app, ui
from datetime import datetime
from pathlib import Path
import secrets, random, string, csv
from manipulate_gsheet import get_sheets_service, append_data, modify_data, delete_row, read_data

###############################################
# TODOS
###############################################
# TODO Implement the "gsheet current data" update advice from gemini

# --LAYOUT & ELEMENTS VARIABLES--
generated_pwd_label: ui.label = None

###############################################
# GENERAL SCOPE VAR AND CONSTANT VAR
###############################################

# --STORING STATE DATA VARIABLES--
# Dict to store at highest scope data used by functions
state: dict[str, str, str, int, tuple] = {
    "generated_pwd": None,
    "today": None,
    "account_name": None,
    "desired_length": None,
}

# --CONSTANT VARIABLES FOR RANDOM CHARS GENERATION--
MIN_PWD_LENGTH = 8
AUTHORIZED_CHARS = string.ascii_letters + string.digits + string.punctuation  # Set up all the available chars
CHAR_LOWER = string.ascii_lowercase  # List of every lowercase char
CHAR_UPPER = string.ascii_uppercase
CHAR_DIGITS = string.digits
CHAR_PUNCTUATION = string.punctuation

# --CONSTANT VARIABLES FOR CSV FILE ACCESS--
SCRIPT_DIR = Path(__file__).parent  # Find the file in current dir
CSV_FILE_PATH = SCRIPT_DIR / "passwords.csv"  # Find the csv file

# --CONSTANT VARIABLES FOR GOOGLE SHEET ACCESS--
SPREADSHEET_ID: str = "1E7YogxyTbP4kENkD22nNk59xZBIzSe6tnh0jd2FxUhY"
SHEET_NAME: str = "Sheet1"
CELLS_RANGE: str = "Sheet1!A1:C"
SERVICE = get_sheets_service()


###############################################
# FUNCTIONS
###############################################
# --CLI/DATA FUNCTIONS --
def random_pwd_generator(length: int) -> str:
    """Generates a random password ensuring character diversity."""
    # List of each kind char
    compulsory_char_diversity: list = [
        secrets.choice(CHAR_LOWER),
        secrets.choice(CHAR_UPPER),
        secrets.choice(CHAR_DIGITS),
        secrets.choice(CHAR_PUNCTUATION)
    ]

    # Fill the password with compulsory chars + the rest of available characters by randoms chars chosen
    # from authorized chars
    if length:
        password_list = list(compulsory_char_diversity)  # Start with required chars
        remaining_length = length - len(password_list)
        password_list.extend([secrets.choice(AUTHORIZED_CHARS) for _ in range(
            remaining_length)])  # Append the initial list with an other list of other random chars

        # Shuffle the list of chosen chars to be sure that the compulsory chars are not everytime at start
        random.shuffle(password_list)

        # Join the list of chars and return the generated pwd
        shuffled_pwd: str = "".join(password_list)
        return shuffled_pwd


# --CSV FILE RELATED FUNCTIONS -- (archives)
def save_to_csv(today: str, account: str, pwd: str) -> None:
    """Saves the provided credentials to a CSV file."""
    data_to_save: tuple = (today, account, pwd)

    # Prevent saving to csv if one or several values are None in "state" dict
    if None in data_to_save:
        generated_pwd_output.set_text(f"🛑 Can't save invalid data")
    else:
        try:
            #  'a' ensures that you add to the end of the file instead of overwriting it.
            #  newline='' prevents blank rows from being added between your data.
            with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
                # Create a csv writer object
                csv_writer = csv.writer(csvfile)

                # Write the new row of data from your tuple
                csv_writer.writerow(data_to_save)
            generated_pwd_output.set_text(f"✅ Successfully save to file")

        except FileNotFoundError:
            generated_pwd_output.set_text(f"🛑Error: The file was not found at {CSV_FILE_PATH}")
        except Exception as e:
            generated_pwd_output.set_text(f"🛑An error occurred: {e}")


# --GUI HANDLING FUNCTIONS --
def handle_generate_pwd_btn() -> None:
    """Handler for the 'Generate' button click event."""

    # Test if length input value by user is an int, or not
    try:
        desired_length: int = int(pwd_length_input.value)
        state["desired_length"] = desired_length
    except (ValueError, TypeError):
        generated_pwd_output.set_text(f"⚠️ Provide an integer")
        # Keep the general scope dict with None values to prevent save_to_csv() function to work properly
        state["desired_length"] = None
        state["generated_pwd"] = None

    if state["desired_length"] <= MIN_PWD_LENGTH:
        generated_pwd_output.set_text(f"⚠️ Provide a number > {MIN_PWD_LENGTH}")
        # Keep the general scope dict "state" with None values to prevent save_to_csv() function to work properly
        state["generated_pwd"] = None
    else:
        # Fill up the "state" dict with the correct values
        state["today"]: str = datetime.today().strftime('%Y-%m-%d')
        state["account_name"]: str = account_spec_input.value
        state["generated_pwd"] = random_pwd_generator(state["desired_length"])
        generated_pwd_output.set_text(f"{state["generated_pwd"]}")


def handle_save_btn_csv_version() -> None:
    return save_to_csv(
        today=state["today"],
        account=state["account_name"],
        pwd=state["generated_pwd"])


def handle_save_btn_gsheet_version():
    today = state["today"]
    account = state["account_name"]
    pwd = state["generated_pwd"]
    data_to_save: list = [[today, account, pwd]]  # The API expects a list of list, or a list of rows
    append_data(service=SERVICE, spreadsheet_id=SPREADSHEET_ID, range_name=SHEET_NAME, data=data_to_save)


def search_account_cred_return_pwd(searched_value: str, data: list) -> list:
    """Look inside the gSheet and return list of save data related to searched value"""
    all_rows_found: list = [sub_list for sub_list in data if searched_value in sub_list]
    # In my current app it will always be the first case because I try to have unique passwords in my gSheet
    if len(all_rows_found) == 1:
        return all_rows_found[0]
    else:
        return all_rows_found


def handle_search_pwd_btn(searched_value: str):
    """Print in the GUI the found password for searched value, or nothing if account does not exist"""
    pwd_found_label.set_text("")
    current_gsheet_data: list = read_data(service=SERVICE, range_name=CELLS_RANGE,
                                          spreadsheet_id=SPREADSHEET_ID)
    row_found: list = search_account_cred_return_pwd(searched_value=searched_value, data=current_gsheet_data)
    if not row_found:
        pwd_found_label.set_text("⚠️ No password associated.")
    else:
        pwd_found_label.set_text(row_found[2])


# --GENERAL GUI FUNCTIONS --
def shutdown_app() -> None:
    """Displays a goodbye message and shuts down the app."""
    goodbye_box = ui.dialog()
    with goodbye_box:
        with ui.card().classes("text-xl font-bold"):
            ui.label("Bye bye!")
    goodbye_box.open()
    app.shutdown()


def close_app() -> None:
    return shutdown_app()


###############################################
# GUI LAYOUT AND RUN
###############################################
with ui.column().classes("w-full h-screen flex-col justify-center items-center"):
    with ui.row():
        # PASSWORD GENERATOR COLUMN
        with ui.column().classes(
                "border-2 border-solid border-red-500 rounded-md  text-lg px-10 py-10 justify-center items-center"):
            with ui.card().classes("shadow no-border mb-4"):
                pwd_length_label = ui.label("Password length:")
                pwd_length_input = ui.input("Integers only")
            with ui.card().classes("shadow no-border mb-4"):
                account_spec_label = ui.label("Used for:")
                account_spec_input = ui.input("Account or software name")
            generate_pwd_btn = ui.button(text="Generate password", on_click=lambda: handle_generate_pwd_btn())
            with ui.card().classes("shadow no-border mb-4 mt-4"):
                generated_pwd_label = ui.label("Generated password:")
                generated_pwd_output: ui.label = ui.label()
            with ui.card().classes("no-shadow no-border"):
                save_pwd_info_btn = ui.button("Save to file",
                                              on_click=handle_save_btn_gsheet_version)
                # ARCHIVE csv saving
                # save_pwd_info_btn = ui.button("Save to file",
                # on_click=handle_save_btn_csv_version)  # Here it is a var name (not a function call)
                # because the handle_save_btn() function (see before) calls a function that will return data and store
                # it in that variable

        # PASSWORD SEARCHING TOOL
        with ui.column():
            with ui.column().classes(
                    "border-2 border-solid border-blue-500 rounded-md  text-lg px-10 py-10 justify-center items-center"):
                with ui.card().classes("shadow no-border mb-4"):
                    search_account_label = ui.label("Searched account:")
                    searched_account_input = ui.input("Type name of your account")
                with ui.card().classes("shadow no-border mb-4"):
                    pwd_found_title = ui.label("Password found:")
                    pwd_found_label = ui.label()
                generate_pwd_btn = ui.button(text="Search password", on_click=lambda: handle_search_pwd_btn(
                    searched_value=searched_account_input.value))

            close_app_btn = ui.button(text="Close app", on_click=close_app).props("color=red stretch")

ui.run()
