#############################################
"""
GET NUMBERS FROM TXT FILE AND COMPUTE AVERAGE OF THOSE NUMBERS
"""
#############################################
def store_file_data_into_list(filename : str) -> list :
    with open(filename,"r") as file:
        data : list = file.readlines()
        return data

def separate_title_from_numbers(data_list: list) -> tuple :
    title : str = data_list[0]
    data_numbers : list = data_list[1:]
    return title,data_numbers # A tuple of 2 values (at 0 index = title ; at 1 index = list of the numbers)

def compute_average(numbers : list) -> float :
    int_numbers : list = [int(number) for number in numbers]
    average : float = sum(int_numbers) / len(numbers)
    return round(float(average),2)

# Main part of the  program
def get_numbers_from_file_and_compute_average(file_directory : str) -> None :
    file_data : list = store_file_data_into_list(file_directory)
    structured_file_data : tuple = separate_title_from_numbers(file_data)

    original_title : str = structured_file_data[0]
    formatted_title : str = original_title.replace("\n","")

    original_numbers: list = structured_file_data[1]
    formatted_numbers : list = [int(number.replace("\n","")) for number in original_numbers]

    average : float = compute_average(formatted_numbers)

    print(f'Your file was about: "{formatted_title}".\n'
          f'The registered data was: {formatted_numbers}.\n'
          f'The computed average is: {average}.')

get_numbers_from_file_and_compute_average("compute_average_from_file_data/data.txt")