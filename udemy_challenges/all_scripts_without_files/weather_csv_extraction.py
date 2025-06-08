import glob # Module to find type of files in directories
import csv # Module to manage csv files

# Extract from my computer Downloads folder all the .csv files
all_csv_files : list = list(glob.glob("/Users/sevakkulinkian/downloads/*.csv"))

# Find the csv file that is about Weather
weather_file : list = []
for file in all_csv_files :
    if "weather" in file :
        weather_file.append(file)

# Extract the data from the found weather file
with open(f"{weather_file[0]}", "r") as file :
    data : list = list(csv.reader(file))

# Extract header and rows to build later a dictionary
header = data[0] # → extract sublist ["City", "Temperature", "Humidity"]
rows = data[1:] # → extract sublist of data of each city

# Create a list of dictionaries, output looks like
# [ {'City': 'Paris', 'Temperature': '30.2', 'Humidity': '49'},
# {'City': 'New York', 'Temperature': '19.9', 'Humidity': '61'}, ... etc...]
list_of_city_dictionaries = [dict(zip(header, row)) for row in rows]
city_list_from_csv : list = [item["City"] for item in list_of_city_dictionaries]

chosen_city = input("Chose your city: ")

def weather_city_data(city_name : str) -> str :

    if city_name in city_list_from_csv :
        row_index : int = city_list_from_csv.index(chosen_city)

        chosen_city_data : dict = list_of_city_dictionaries[row_index]
        return (f"Data for {chosen_city_data["City"]} is : \n"
                f"- Temperature: {chosen_city_data["Temperature"]}°C\n"
                f"- Humidity: {chosen_city_data["Humidity"]}HpA")
    else :
        return (f"{city_name} is not part of the csv file.\n"
                f"The list of existing cities is: {", ".join(city_list_from_csv)}")

# print(weather_city_data(chosen_city))


"""Other way to create a Dictionary from a csv file"""
with open(f"{weather_file[0]}", "r") as file :
    data_dict_v2 : list = list(csv.DictReader(file))
print(data_dict_v2)

"""Other way to create a List from a csv file"""
with open(f"{weather_file[0]}", "r") as file :
    data_dict_v3 : list = list(csv.reader(file))
print(data_dict_v3)



