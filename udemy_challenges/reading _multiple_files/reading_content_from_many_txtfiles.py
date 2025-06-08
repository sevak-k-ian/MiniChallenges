#############################################
"""
Exercice 5
Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.
Then, create a program that:
1. reads each text file and
2. prints out the content of each file in the command line."""
#############################################

import os
files : list = os.listdir("reading _multiple_files")
sorted_files : list = sorted(files)

def exe_5() -> None :
    for filename in sorted_files :
        file = open(f'reading _multiple_files/{filename}', "r")
        content : str = file.read()
        file.close()
        print(content)

exe_5()