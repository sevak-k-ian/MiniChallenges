#############################################
"""BUILD AN AGE CALCULATOR
Write a Python program that:
- Asks the user to enter their birth year
- Asks for the current year
- Calculates the user's age
- Prints the result
Expected Output: The program prompts the user to enter their year of birth
and the current year and then it returns a message with the user's age.
"""
#############################################

def compute_years(birth_year, current_year) -> int :
    num_birth_year : int = int(birth_year)
    num_current_year : int = int(current_year)
    result : int = num_current_year - num_birth_year
    return result

def age_calculator_program() -> str :
    birth_year : str = input("Enter your birth year (for example : 20XX): ")
    current_year: str = input("Enter the current year : ")
    age : int = compute_years(birth_year, current_year)
    print(f'You are {age} years old ({current_year} -  {birth_year} = {age}).')

# age_calculator_program()
