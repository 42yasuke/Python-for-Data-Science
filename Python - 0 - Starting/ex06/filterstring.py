import sys
import string
from ft_filter import ft_filter


def filterString(strg, length):
    """
    Filter words in a string based on their length.

    Parameters:
        strg (str): Input string containing words.
        length (str): Length threshold as a string.

    Returns:
        list: List of words with length greater than or
        equal to the specified length.
    """
    tmp = [x for x in strg.split()]
    result = list(ft_filter(lambda x: len(x) >= length, tmp))
    return result


def testingArgs():
    """
    Validate command-line arguments.

    Raises AssertionError if:
    - The number of arguments is not exactly 3.
    - The second argument is not a digit.
    - The first argument contains any punctuation characters.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    strg, length = sys.argv[1], sys.argv[2]
    if not length.isdigit():
        raise AssertionError("the arguments are bad")
    elif not strg.isprintable():
        raise AssertionError("the arguments are bad")
    else:
        for i in strg:
            if i in string.punctuation:
                raise AssertionError("the arguments are bad")


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
        print(filterString(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
