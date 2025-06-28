# Ask the user to input an email address.
def get_email_from_user() -> str :
    user_input : str = input("Give an email address: ")
    return user_input

# Use a regular expression to validate if it has the correct format (like someone@example.com).
import re

def is_valid_email(email: str):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Print whether it’s valid or not.
def print_email_validity(validity:bool) -> str :
    if validity:
        print("Correct email")
    else :
        print("Wrong email")

def main_prog() -> None :
    email_input : str = get_email_from_user()
    is_valid : bool = is_valid_email(email=email_input)
    print_email_validity(is_valid)

main_prog()