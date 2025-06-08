#############################################
"""
Python Project: Analyze Text with Python
Task: Write a Python script that takes a user-inputted block of text and analyzes it by calculating the number of characters, words, and sentences. Additionally, determine the most frequently used word and calculate the average word and sentence length.
The program should output text statistics, including:
- Total Characters
- Total Words
- Total Sentences
- Most Frequent Word
- Average Word Length
- Average Sentence Length
"""
#############################################
# Import Regex module
import re

text_to_analyze : str = "Trees usually reproduce using seeds. Flowering plants have their seeds inside fruits, while conifers carry their seeds in cones, and tree ferns produce spores instead."

def get_text_block() -> str :
    text : str = input("Fournis moi un texte complet: ")
    return text

# Total characters
def count_char(text) -> int :
    no_space_text = text.lower().replace(" ", "")
    num_chars = len(no_space_text)
    return num_chars

# Find all words from text and store it into list
regex_word : str = r"\b\w+\b"

def match_words(text) -> list :
    return re.findall(regex_word,text)

# Count words stored inside a list
def count_words(list) -> int :
    return len(list)


# Find all sentences from text and store it into list
regex_sentence : str = r"[^.!?]*[.!?]"
def match_sentences(text) -> list :
    return re.findall(regex_sentence,text)

# Count sentences stored inside a list
def count_sentences(list) -> int :
    return len(list)


# Most frequent word
from collections import Counter

def most_common_word(list) -> str :
    result : list = Counter(list).most_common(1)
    most_used_word : str = result[0][0]
    num_of_times_used : str = str(result[0][1])
    return most_used_word,num_of_times_used   #singe tuple returned


# Average word length
def average_word_size(list) -> float :
    average = sum(len(word) for word in list)  / len(list)
    return round(average,2)


# Average sentence length
def average_sentence_size(list) -> float :
    size_of_sentences : list = []
    # Create a list of all sizes of all sentences
    for sentence in list :
        size_of_sentences.append(count_words(match_words(sentence)))
    # Compute average size thanks to the list of sizes
    for i in size_of_sentences :
        average = sum(i for i in size_of_sentences) / len(size_of_sentences)
    return round(average,2)



def main() -> None :
    text : str = get_text_block()
    print("Text block received ✅\nTEXT ANALYSIS RESULTS\n-----------------")

    list_words : list = match_words(text)
    list_sentences : list = match_sentences(text)

    print(f'Total words: {count_words(list_words)}')
    print(f'Total sentences: {count_sentences(list_sentences)}')

    most_occurence : tuple = most_common_word(list_words)
    print(f'The most common word is : "{most_occurence[0]}". This word appeared {most_occurence[1]} times.')

    print(f'Average word length is: {average_word_size(list_words)} characters.')
    print(f'Average sentence length is: {average_sentence_size(list_sentences)} words.')

    print("-----------------")

# main()