import sys
import string


def testingArgs():
    """
    Validate command-line arguments.

    Raises AssertionError if:
    - The number of arguments is not exactly 2.
    - The first argument contains any non-alphanumeric characters.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    strg = sys.argv[1]
    alphanum = string.ascii_letters + string.digits + ' '
    for i in strg:
        if i not in alphanum:
            raise AssertionError("the arguments are bad")


def morseCode(strg):
    """
    Convert a string to Morse code.

    Parameters:
        strg (str): Input string to be converted.

    Returns:
        str: Morse code representation of the input string.
    """
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    result = []
    for char in strg.upper():
        result.append(MORSE_CODE_DICT[char])
    return ' '.join(result)


def main():
    """
    Main function to execute the filterString function
    with command-line arguments.
    Handles AssertionError and prints appropriate messages.
    """
    try:
        testingArgs()
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
    else:
        print(morseCode(sys.argv[1]))


if __name__ == "__main__":
    main()
