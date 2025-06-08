#############################################
"""
COUNTDOWN TIMER
Write a Python program that:
- Asks the user to input a duration in seconds
- Displays a countdown timer in mm:ss format
- Prints a message when the timer is done
- Expected Output: The program will ask the user to enter a value for seconds (e.g., 10):
"""
#############################################
# Asks the user to input a duration in seconds
def get_input() -> int :
    try :
        seconds_input : int = int(input(f'Enter the time in seconds: '))
        return seconds_input
    except ValueError :
        return f'⚠️ Please provide seconds in integer'

# Display input into mm:ss format
from datetime import timedelta
def display_mm_ss_format(sec_input : int) -> str :
    formatted_time : str = timedelta(seconds=sec_input)
    return formatted_time


###### MAIN PROGRAM
###################
from time import sleep

def countdown() -> str :
    while True :
        try :
            sec_input : int = get_input()
            reversed_time_range : list = list(reversed([i for i in range (1,sec_input +1)]))

            for sec in reversed_time_range :
                mm_ss: str = display_mm_ss_format(sec)
                print(mm_ss)
                sleep(1)
            return f"Time's up!"

        except TypeError :
            print(f'⚠️ Please provide seconds in integer')


# print(countdown())


#############################################
"""
SECOND VERSION USING RANGE()
"""
#############################################
def countdown_v2() -> str :
    while True :
        try :
            sec_input : int = get_input()

            for sec in range(sec_input, 0, -1) :
                mm_ss: str = display_mm_ss_format(sec)
                print(mm_ss)
                sleep(1)
            return f"Time's up!"

        except TypeError :
            print(f'⚠️ Please provide seconds in integer')

# print(countdown_v2())
