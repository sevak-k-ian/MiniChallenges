
#############################################
"""Create a program that:
(1) prompts the user to input their name,
(2) prints out the name with the first letter capitalized,
(3) keeps prompting the user to input another name
(4)  prints out the name with the first letter capitalized,
(5) The process is repeated infinitely.
The screenshot below shows how the program should behave when run:"""
#############################################

def get_name():
    input_name : str = input("What's your name? ")
    return input_name

def exit_prompt():
    answer = input("You wanna stop? Press Yes or No ")
    return answer

while True :
    name : str = get_name()
    cap_name : str = name.capitalize()
    print(cap_name)

    if exit_prompt() == "Yes":
        print("Ok, bye bye!")
        break