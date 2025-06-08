#############################################
"""
TRANSFORM LIST OF STRINGS
Transform the following provided list of string into the following output :
["1-doc.txt", "1-report.txt", "1-presentation.txt"]
"""
#############################################

provided_filenames : list = ["1.doc", "1.report", "1.presentation"]

# 1st solution with Looping
formatted_filenames : list = []
for filename in provided_filenames :
    formatted_filename : str = filename.replace(".","-") + ".txt"
    formatted_filenames.append(formatted_filename)

print(formatted_filenames)

# 2nd solution with List Comprehension
formatted_filenames_2 : list = [filename.replace(".","-") + ".txt" for filename in provided_filenames]
print(formatted_filenames_2)

