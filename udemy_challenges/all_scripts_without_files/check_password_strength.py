#############################################
"""
CHECK STRENGTH OF A PASSWORD
Programm will :
- get password input from user
- print "Strong password" if min 8 chars + 1 capital letter + 1 digit
- print "Weak password" + tells the conditions not fullfiled
"""
#############################################

# Check len of string > 8 chars
def len_sup_8(password : str) -> bool:
    if len(password) > 8 :
        return True
    else :
        return False

# Check if 1 capital letter exists
def contains_cap_letter(password : str) -> bool:
    has_cap_letter = any(char.isupper() for char in password)
    return has_cap_letter

# Check if 1 digit is here
def contains_digit(password : str) -> bool:
    has_digit = any(char.isdigit() for char in password)
    return has_digit

# Main Programm
def strength_check_password() -> None :
    while True :
        password: str = input("Type your password : ")
        if len_sup_8(password) and contains_cap_letter(password) and contains_digit(password) :
            print("✅You provided a strong password.")
            break
        else :
            print(f'Min 8 characters : {"✅" if len_sup_8(password) else "🛑"}\n'
                  f'Cap letter : {"✅" if contains_cap_letter(password) else "🛑"}\n'
                  f'Digit : {"✅" if contains_digit(password) else "🛑"}'
                  )

strength_check_password()

"""SAME EXERSICE BUT RESOLVED WITH DICTIONARIES"""

def strength_check_password_2() :
    password: str = input("Type your password : ")
    password_strength: dict = {}

    if len(password) > 8 :
        password_strength["length"] = True
    else :
        password_strength["length"] = False

    if any(char.isupper() for char in password) :
        password_strength["upper"] = True
    else :
        password_strength["length"] = False

    if any(char.isdigit() for char in password) :
        password_strength["digit"] = True
    else :
        password_strength["digit"] = False

    if all(password_strength.values()) == True :
        print("✅You provided a strong password.")
    else :
        for tuple in password_strength.items() :
            print(tuple)

# strength_check_password_2()
