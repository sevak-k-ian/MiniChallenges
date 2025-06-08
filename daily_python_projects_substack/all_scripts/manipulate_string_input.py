#############################################
"""
Python Project: Manipulating User Input Text
Write a Python program that:
- Accepts a user's full name as input
- Prints the name in uppercase and lowercase
- Removes spaces and counts the characters
- Reverses the name
"""
#############################################
# FUNCTIONS USED
# Get user's input
def get_input() -> str :
    name : str = input("Donne moi un nom complet: ")
    return name

# Print in uppercase & lowercase, side-by-side
def print_upper_lower(name) -> None :
    upper_name : str =  name.upper()
    lower_name : str = name.lower()
    print(f'La version majuscule est: {upper_name} // La version en minuscule: {lower_name}' )

# Removes spaces & counts the characters side-by-side
def remove_count_char(name) -> None :
    no_space_name : str = name.lower().replace(" ","")
    num_chars : int = len(no_space_name)
    print(f'Il y a  {num_chars} lettres dans le nom complet "{no_space_name}"')

# Main
def main() -> None :
    name = get_input()
    print_upper_lower(name)
    remove_count_char(name)

# main()


