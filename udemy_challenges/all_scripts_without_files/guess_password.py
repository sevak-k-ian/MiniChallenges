#############################################
"""Asking for a password until I got the correct one"""
#############################################

password_to_find : str = "Sévak"

# MAIN CODE OF THE CHALLENGE 
while True :
     guess = input("Guess the password")
     if password_to_find == guess :
         break

print(guess)