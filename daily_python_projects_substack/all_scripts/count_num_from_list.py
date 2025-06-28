# Get input from user separated by comma, and print error message if not good format provided
def get_list_of_nums() -> list:
    while True:
        user_input: str = input("Enter a list of num separated by commas :")
        try:
            list_of_int: list = [int(num.strip()) for num in user_input.split(",")]
            return list_of_int
        except ValueError:
            print("Wrong input start over")


# Get the num that the person wants to count and print error message if not good format provided
def what_num_to_count() -> int:
    while True:
        num_to_count: str = input("Enter the num you want to count: ")
        try:
            num_int: int = int(num_to_count)
            return num_int
        except ValueError:
            print("Wrong input start again.")


def num_counter(list_of_nums: list, num_to_count: int) -> str:
    occurrence: int = list_of_nums.count(num_to_count)
    return occurrence


# Print a sentence where the result is correctly displayed
def main_prog() -> None:
    user_list: list = get_list_of_nums()
    print(user_list, type(user_list))
    num_to_find: int = what_num_to_count()
    print(num_to_find, type(num_to_find))
    occurrence: int = num_counter(list_of_nums=user_list, num_to_count=num_to_find)
    print(occurrence, type(occurrence))
    print(f"The num {num_to_find} appears {occurrence} times in the list you provided")


main_prog()
