import sys
import string


def count_characters(text: str) -> None:
    """
    Counts and prints the number of upper-case, lower-case,
    punctuation, digit, and space characters in the given string.
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c == ' ' or c == '\n')
    digits = sum(1 for c in text if c.isdigit())
    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Entry point: reads one string argument or prompts the user.
    Raises AssertionError if more than one argument is provided.
    """
    try:
        args = sys.argv[1:]
        assert len(args) <= 1, "more than one argument is provided"
        if len(args) == 1:
            text = args[0]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()
        count_characters(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
