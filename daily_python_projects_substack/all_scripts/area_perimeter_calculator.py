"""
PERIMETER AND AREA CALCULATOR
- Defines a function to calculate the area of a rectangle
- Defines another function to calculate the perimeter
- Calls both functions with sample inputs
- Prints the results"""

def area(length : float, width : float) -> float :
    return length * width

def perimeter(length : float, width : float) -> float :
    return (length*2) + (width*2)

def get_user_data() -> str :
    return input("Provide me a length and a width of a rectangle: ")

def parse_user_data(prompted_data : str) -> tuple :
    parsed_data : list = prompted_data.split()
    return parsed_data[0], parsed_data[1]

def main_calculator() -> str :
    user_data : str = get_user_data()
    length, width = parse_user_data(user_data)

    length_user = float(length)
    width_user = float(width)

    area_user : float = area(length_user, width_user)
    perimeter_user : float = perimeter(length_user, width_user)

    print(f"Provided value : {length_user} (length) and {width_user} (width)\n"
          f"Area = {area_user}\n"
          f"Perimeter = {perimeter_user}")

main_calculator()
