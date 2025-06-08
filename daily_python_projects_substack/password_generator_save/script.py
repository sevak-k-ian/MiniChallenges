from nicegui import app, ui

# TODOS
# TODO Ask Google to improve code performance and logic without adding for the moment comments
# TODO Ask Google to comment everything

# --LAYOUT & ELEMENTS VARIABLES--
pwd_length_label: ui.label = None
pwd_length_input: ui.input = None
account_spec_label: ui.label = None
account_spec_input: ui.input = None
generate_pwd_btn: ui.button = None
generated_pwd_label: ui.label = None
save_pwd_info_btn: ui.button = None

# --STORING DATA VARIABLES--
generated_pwd: str = None
data_to_save_to_csv: tuple = None
csv_abs_path: str = "/Users/sevakkulinkian/PycharmProjects/MiniChallenges/daily_python_projects_substack/password_generator_save/passwords.csv"


# Enter the desired password length
def get_desired_length() -> int:
    try:
        desired_length: int = int(pwd_length_input.value)
        return desired_length
    except ValueError:
        print("⚠️Not an integer provided!")


def account_software_used() -> str:
    user_input: str = account_spec_input.value
    return user_input


import secrets
import random
import string


def random_pwd_generator(length: int) -> str:
    # 1. Set up all the available chars for my generators
    authorized_chars = string.ascii_letters + string.digits + string.punctuation

    # 2. Ensure that at least there will be one char of each kind
    compulsory_char_diversity: list = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.punctuation),
        secrets.choice(string.digits)
    ]

    # 3. Fill the password with compulsory chars + the rest of available characters by randoms chars choosen from authorized chars
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


import csv


def save_data_to_csv(data_to_save: tuple) -> None:
    try:
        #  'a' ensures that you add to the end of the file instead of overwriting it.
        #  newline='' prevents blank rows from being added between your data.
        with open(csv_abs_path, 'a', newline='') as csvfile:
            # Create a csv writer object
            csv_writer = csv.writer(csvfile)

            # Write the new row of data from your tuple
            csv_writer.writerow(data_to_save)
        print("Successfully added new data to passwords.csv")

    except FileNotFoundError:
        print(f"Error: The file was not found at {csv_abs_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


from datetime import datetime


def handle_generate_pwd_btn() -> None:
    # Generated data to store then in csv file
    global generated_pwd
    today: str = datetime.today().strftime('%Y-%m-%d')
    account: str = account_software_used()
    length = get_desired_length()
    if not isinstance(length, int):
        generated_pwd_output.set_text(f"⚠️ Provide an integer")
    elif length <= 8:
        generated_pwd_output.set_text(f"⚠️ Provide a number > 8")
    else:
        generated_pwd = random_pwd_generator(length)
        generated_pwd_output.set_text(f"{generated_pwd}")
        global data_to_save_to_csv
        data_to_save_to_csv = (today, account, generated_pwd)
        return data_to_save_to_csv


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
                                          on_click=lambda: save_data_to_csv(data_to_save=data_to_save_to_csv))
            close_app_btn = ui.button(text="Close app", on_click=lambda: shutdown_app()).props("color=red stretch")

ui.run()
