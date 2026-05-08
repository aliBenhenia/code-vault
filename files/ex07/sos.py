import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
}


def encode_morse(text: str) -> str:
    """
    Encodes a string into Morse code using the NESTED_MORSE dictionary.
    Supports alphanumeric characters and spaces.
    """
    return "".join(NESTED_MORSE[c.upper()] for c in text)


def main():
    """
    Entry point: reads one string argument and encodes it to Morse code.
    Raises AssertionError if argument count != 1 or contains invalid chars.
    """
    try:
        args = sys.argv[1:]
        assert len(args) == 1, "the arguments are bad"
        text = args[0]
        assert all(
            c.upper() in NESTED_MORSE for c in text
        ), "the arguments are bad"
        print(encode_morse(text))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
