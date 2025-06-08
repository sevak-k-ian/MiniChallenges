#############################################
"""create a program that:
1. generates multiple text files by iterating over the filenames list,
2. and writes the text Hello  inside each generated text file."""
#############################################

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

def write_hello_in_files() -> None :
    for filename in filenames :
        file = open(f'/Users/sevakkulinkian/Documents/PYTHON/Hello_files/{filename}',"w")
        file.write("Hello")
        file.close()

write_hello_in_files()