morse_code_dict : dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Used to separate words
}
def encoder() -> str :
    string_to_code: str = input("Ecris ta phrase à encoder: ")
    global morse_code_dict
    encoded_phrase : str = ""
    for char in string_to_code :
        print(morse_code_dict[f"{char.upper()}"])
    #     if char.isalpha() :
    #         encoded_phrase = encoded_phrase + morse_code_dict[f"{char.upper()}"]
    #     else :
    #         encoded_phrase = encoded_phrase + morse_code_dict[char]
    # return encoded_phrase

# encoder()

def sum_range(num_begin : int, num_end : int) -> int :
    result : int = 0
    for num in range(num_begin, num_end+1):
        result += num
    return result

print(sum_range(1, 100))