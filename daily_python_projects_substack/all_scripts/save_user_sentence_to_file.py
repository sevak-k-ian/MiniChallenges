########################################################
# Write a Python program that:
# - Prompts the user to enter three different sentences
# - Writes each sentence to a file, separated by a dashed line (-----------) except after the last one
# - Saves the content to a file named user_sentences.txt
########################################################


##### SECOND ALTERNATIVE SOLUTION /// VERY SHORT AND EFFICIENT
filename = "user_sentences.txt"
sentences = [input(f"Enter sentence {i+1}: ") for i in range(3)]

with open(filename, "w") as file:
    for i, sentence in enumerate(sentences):
        file.write(sentence + "\n")
        if i < 2:
            file.write("-----------\n")

print(f"Saved 3 sentences to {filename}.")



# Prompt user to enter 3 different sentences
def get_input() -> list :
    # Get a correct integer to know number of sentences wanted
    while True :
        try:
            number_of_sentences : int = int(input("How many sentences you want to provide? "))
            break
        except ValueError :
            print("Provide a integer please.")
    sentences : list = []
    # Gather input sentences inside a list
    while len(sentences) < number_of_sentences :
        sentence : str = input("Write your sentence: ")
        sentences.append(sentence)
    return sentences

# Format the 3 sentences according to desired format
def format_sentences(provided_sentences : list) -> list :
    formatted_sentences : list = []
    # Loop all items of provided_sentences list except last one
    for sentence in provided_sentences[0:len(provided_sentences)-1:1] :
        new_sentence : str = sentence + "\n---------\n"
        formatted_sentences.append(new_sentence)
    # Add to new formatted_sentences the last item of provided_sentences without the dash lines
    formatted_sentences.append(provided_sentences[len(provided_sentences)-1])
    return formatted_sentences

# Open a named user_sentences.txt to write inside the formatted sentences
def write_new_txt_file(text_to_write : list) -> None :
    with open("../write_formatted_user_sentences/named user_sentences.txt", "w") as file :
        file.writelines(text_to_write)


# MAIN PROGRAM
def main() -> None :
    user_sentences : list = get_input()
    formatted_user_sentences : list = format_sentences(user_sentences)
    write_new_txt_file(formatted_user_sentences)

main()

##### ALTERNATIVE SOLUTION
# Define the file name
filename = "user_sentences.txt"

# Open the file in write mode
with open(filename, "w") as file:
    # Loop three times to get sentences from the user
    for i in range(3): # or len(size_wanted)
        # Prompt the user to enter a sentence
        sentence = input(f"Enter sentence {i+1}: ")
        # Write the sentence to the file
        file.write(sentence + "\n")
        # If it's not the last sentence, add dash lines
        if i < 2:
            file.write("-----------\n")

print(f"Sentences have been saved to {filename}.")


