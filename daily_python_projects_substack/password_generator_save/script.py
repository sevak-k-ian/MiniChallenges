from nicegui import app, ui
from datetime import datetime
import secrets, random, string, csv, os

# TODOS
# TODO Ask Google to comment everything
# TODO Push changes

# --LAYOUT & ELEMENTS VARIABLES--
generated_pwd_label: ui.label = None

# --STORING STATE DATA VARIABLES--
state: dict[str, str, str, int, tuple] = {
    "generated_pwd": None,
    "today": None,
    "account_name": None,
    "desired_length": None,
}

# --STORING CONSTANT DATA VARIABLES--
MIN_PWD_LENGTH = 8
CHAR_LOWER = string.ascii_lowercase
CHAR_UPPER = string.ascii_uppercase
CHAR_DIGITS = string.digits
CHAR_PUNCTUATION = string.punctuation
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = f"{SCRIPT_DIR}/passwords.csv"


# Enter the desired password length
def get_desired_length() -> int:
    try:
        desired_length: int = int(pwd_length_input.value)
        return desired_length
    except ValueError:
        None


def account_software_used() -> str:
    user_input: str = account_spec_input.value
    return user_input


def random_pwd_generator(length: int) -> str:
    # 1. Set up all the available chars for my generators
    authorized_chars = string.ascii_letters + string.digits + string.punctuation

    # 2. Ensure that at least there will be one char of each kind
    compulsory_char_diversity: list = [
        secrets.choice(CHAR_LOWER),
        secrets.choice(CHAR_UPPER),
        secrets.choice(CHAR_DIGITS),
        secrets.choice(CHAR_PUNCTUATION)
    ]

    # 3. Fill the password with compulsory chars + the rest of available characters by randoms chars chosen from authorized chars
    if length:
        password: list = []
        for item in compulsory_char_diversity:
            password.append(item)
        for i in range(length - 4):
            password.append(secrets.choice(authorized_chars))

        # 4. Shuffle the list of chosen chars to be sure that the compulsory chars are not everytime at start
        random.shuffle(password)

        # 5. Join the list of chars and return the generated pwd
        shuffled_pwd: str = "".join(password)
        return shuffled_pwd


def save_data_to_csv(today: str, account: str, pwd: str) -> None:
    data_to_save: tuple = (today, account, pwd)

    if any(map(lambda x: x is None, data_to_save)):
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


def handle_generate_pwd_btn() -> None:
    # Update var that stores GUI generated data
    state["today"]: str = datetime.today().strftime('%Y-%m-%d')
    state["account_name"]: str = account_software_used()
    state["desired_length"] = get_desired_length()

    # Logic
    if not isinstance(state["desired_length"], int):
        generated_pwd_output.set_text(f"⚠️ Provide an integer")
    elif state["desired_length"] <= MIN_PWD_LENGTH:
        generated_pwd_output.set_text(f"⚠️ Provide a number > {MIN_PWD_LENGTH}")
    else:
        state["generated_pwd"] = random_pwd_generator(state["desired_length"])
        generated_pwd_output.set_text(f"{state["generated_pwd"]}")


def shutdown_app() -> None:
    goodbye_box = ui.dialog()
    with goodbye_box:
        with ui.card().classes("text-xl font-bold"):
            ui.label("Bye bye!")
    goodbye_box.open()
    app.shutdown()


# --GUI DISPLAY--
with ui.column().classes("w-full h-screen flex-col justify-center items-center"):
    with ui.column().classes(
            "border-2 border-solid border-blue-500 rounded-md  text-lg px-10 py-10 justify-center items-center"):
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
                                          on_click=lambda: save_data_to_csv(today=state["today"],
                                                                            account=state["account_name"],
                                                                            pwd=state["generated_pwd"]))
            close_app_btn = ui.button(text="Close app", on_click=lambda: shutdown_app()).props("color=red stretch")

ui.run()
