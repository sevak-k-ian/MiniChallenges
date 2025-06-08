import FreeSimpleGUI as sg
import zipfile, os


# Setting a theme
sg.theme("TealMono")
text_font: tuple = ("Avenir", 16)

# Widgets variable declaration
select_file_label = sg.Text(text="Select file to compress", font=text_font, pad=((5, 17), (0, 0)))
select_file_input = sg.Input(key="-FILES-", default_text="Multiple files expected", font=text_font)
select_file_btn = sg.FilesBrowse(key="-FILE_BTN-", button_text="Select", font=text_font)

select_destination_label = sg.Text(text="Select destination folder", font=text_font)
select_destination_input = sg.Input(key="-FOLDER-", font=text_font)
select_destination_btn = sg.FolderBrowse(key="-FOLDER_BTN-", button_text="Select", font=text_font)

compress_btn = sg.Button(key="-COMPRESS-", button_text="Compress", font=text_font)
exit_btn = sg.Button(button_text="Exit", font=text_font)

# Layout definition
layout = [
    [select_file_label, select_file_input, select_file_btn],
    [select_destination_label, select_destination_input, select_destination_btn],
    [compress_btn, exit_btn]
]

# Layout rendering in window
window = sg.Window(title="ZIP Folder Maker", layout=layout)

# Loop to listen events
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "-COMPRESS-" :
        files_path_raw = values["-FILES-"]  # semicolon-separated string
        folder_path = values["-FOLDER-"]

        # Split into list of individual files
        files_path = files_path_raw.split(";")

        # Ensure absolute path for output folder
        abs_folder_path = os.path.abspath(folder_path)
        zip_output_path = os.path.join(abs_folder_path, "compressed.zip")

        with zipfile.ZipFile(zip_output_path, mode="w") as my_zip:
            for file in files_path:
                abs_file = os.path.abspath(file.strip())  # strip in case of spaces
                my_zip.write(abs_file, arcname=os.path.basename(abs_file))

        if my_zip :
            sg.popup("Compression finished with success", title="✅Done")


# Close the window
window.close()
