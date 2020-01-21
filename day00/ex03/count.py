import sys


def plural(n):
    return "s" if n > 1 else ""


def text_analyser(string=None):
    """
    This is a lite version of text_analyser.
    """
    if string is None:
        print("What is the text to analyse?")
        string = input(">> ")

    if string is "":
        print("Empty string")

    else:
        upper, lower, space, punct = 0, 0, 0, 0
        for l in string:
            if l.isupper():
                upper += 1
            elif l.islower():
                lower += 1
            elif l in "\t\n\v\f\r ":
                space += 1
            elif l in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{¦}~":
                punct += 1

        print("- {} upper letter{}".format(upper, plural(upper)))
        print("- {} lower letter{}".format(lower, plural(lower)))
        print("- {} punctuation mark{}".format(punct, plural(punct)))
        print("- {} space{}".format(space, plural(space)))
