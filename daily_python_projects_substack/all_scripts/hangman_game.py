# Generate a random password
# pip install wonderwords
from wonderwords import RandomWord


def generate_random_word() -> str:
    """Generate a random word with a specific length provided by the user"""
    user_input: str = input("Enter two numbers separated by spaces: ")
    min_max_length: list = [int(num) for num in user_input.split()]
    r = RandomWord()
    # Return a single random word
    word: str = r.word(word_min_length=min_max_length[0], word_max_length=min_max_length[1])
    print(word)
    return word


def get_distinct_letters(word: str) -> list:
    """Take a word as an arg to store it into 2 different lists : one with visible letters, one with underscores
    representing the word. The 2 lists are returned as a tuple"""
    list_of_letters: list = [char for char in word]
    list_of_crypted_letters: list = ["_" for char in word]
    return list_of_letters, list_of_crypted_letters


def get_user_guess() -> str:
    """Get a letter from user and format it into lower case without whitespaces"""
    letter_input: str = input('Guess a letter: ')
    return letter_input.strip().lower()


def display_chars_to_find(chars_to_find: list, crypted_version: list) -> None:
    """Print the two lists one below each other"""
    print(chars_to_find)
    print(crypted_version)


def game_logic() -> None:
    word_to_find: str = generate_random_word()
    tuple_of_letters: tuple = get_distinct_letters(word_to_find)

    letters_to_find: list = tuple_of_letters[0]
    crypted_letters: list = tuple_of_letters[1]

    counter: int = 0
    max_limit_of_guess: int = 5
    print(f'You will have {max_limit_of_guess} tries to guess the word!')

    while counter < max_limit_of_guess:
        guess: str = get_user_guess()
        # Check if the letter guessed is inside the list or not, and store the found letters, and their index,
        # inside a list
        guessed_value_index: list = [(i, char) for (i, char) in enumerate(letters_to_find) if char == guess]

        # If not letters/index have been found and stored inside the guess_value_index list
        if len(guessed_value_index) == 0:
            counter += 1
            print("Wrong guess")
            print(f'You have {max_limit_of_guess - counter} tries left.')
        # If one or more letters/index have been found and stored inside the guess_value_index list
        else:
            for index_value in guessed_value_index:
                crypted_letters[index_value[0]] = letters_to_find[index_value[0]]
            print("Good guess!")
            print(crypted_letters)

            # Check if there are still letters to find, or not
            if "_" not in crypted_letters:
                print("You discovered every letter, bravo!")
                break
    # If the counter reaches the max limit, break the while loop by printing end message
    else:
        print("You consumed all the tries, and you lost!")


game_logic()
