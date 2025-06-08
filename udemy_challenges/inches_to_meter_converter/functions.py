def parse_user_input() -> tuple :
    """ Ask user to input feet & inches and parse then store it
    into 2 different variable (instead of a tuple) """
    data = input("Give me feet & inches : ")
    parsed_data: list = [float(num) for num in data.split(" ", -1)]
    feet, inch = parsed_data
    return feet, inch

"""
parsed_data is a tuple. 
feet : float = parsed_data[0]
inch: float = parsed_data[1]
I can access the result by 2 ways :
feet=parsed_data[0] and inch=parsed_data[1]
or → feet, inch = parse_user_input()
"""

def convert_to_meter(feet: float, inch: float) -> float:
    result : float = feet * 0.3048 + inch * 0.0254
    return result


if __name__ == "__main__":
    feet, inch = parse_user_input()
    print(feet)
    print(inch)