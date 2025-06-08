#############################################
"""Summing Up Two Numbers from User Input
https://dailypythonprojects.substack.com/p/python-project-summing-up-two-numbers"""
#############################################

# Check if the input data is an integer, or not
def is_number(input_value) :
    try :
        int(input_value)
        return True
    except ValueError :
        return False

# Get the input, and repeat it until the input is a integer
def get_num_from_user(prompt) :
    while True :
        value = input(prompt)
        if is_number(value) :
            return int(value)
        else :
            print("Invalid input! Please enter a number: ")

# Gameplay
def start_the_game() :
    first_num_input = get_num_from_user("Enter your 1st number please : ")
    second_num_input = get_num_from_user("Enter your 2nd number please : ")

    sum_result = first_num_input + second_num_input

    print(f"The sum is {sum_result}")

# Function call to start the game
# start_the_game()
