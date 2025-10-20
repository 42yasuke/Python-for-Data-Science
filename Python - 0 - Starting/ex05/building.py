import sys
import string


def findAllCharAndCountThem(strg):
    """
    Count and print simple character statistics for a string.

    Parameters:
        strg (str): Text to analyze.

    Returns:
        None
    """
    nbSpace = nbUpper = nbLower = nbDigit = nbPunctuation = 0
    nbChar = len(strg)
    for i in strg:
        tmp = str(i)
        if tmp.isspace():
            nbSpace += 1
        elif tmp.isupper():
            nbUpper += 1
        elif tmp.islower():
            nbLower += 1
        elif tmp.isdigit():
            nbDigit += 1
        elif i in string.punctuation:
            nbPunctuation += 1
    print(f"The text contains {nbChar} characters:\n\
            {nbUpper} upper letters\n\
            {nbLower} lower letters\n\
            {nbPunctuation} punctuation marks\n\
            {nbSpace} spaces\n{nbDigit} digits")


def main():
    """
    Main entry point.

    Read text from command-line if one argument is given,
    otherwise read from stdin.
    If more than one argument is given, print an AssertionError message.
    Calls `findAllCharAndCountThem` to display the results.
    """
    strg = ""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            strg = sys.argv[1]
        else:
            print("What is the text to count?")
            strg = sys.stdin.readline()
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
    else:
        if not strg.endswith("\n"):
            print("")
        findAllCharAndCountThem(strg)


if __name__ == "__main__":
    main()
