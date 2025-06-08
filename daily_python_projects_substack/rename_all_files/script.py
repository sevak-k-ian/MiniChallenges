import os
from datetime import datetime

# Get the absolute path of working directory
abs_path_current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the files directory
abs_path_files_dir = os.path.join(abs_path_current_dir, "files/")

# Get today's date in str
today: str = datetime.today().strftime('%Y-%m-%d')

def rename_files() -> None :
    for file in os.listdir(abs_path_files_dir) :
        file_path_source : str = f"{abs_path_files_dir}{file}"
        file_path_destination : str = f"{file_path_source[:-4]}-{today}.txt"

        os.rename(file_path_source, file_path_destination)

        print(f"Renamed '{file}' to '{file[:1]}-{today}.txt'")

    print("File renaming complete.")

rename_files()
