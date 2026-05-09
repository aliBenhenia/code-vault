import sys


def main():
    """
    Takes a number as argument and checks if it is odd or even.
    Prints AssertionError if more than one argument or not an integer.
    """
    try:
        args = sys.argv[1:]
        assert len(args) <= 1, "more than one argument is provided"
        if len(args) == 0:
            return
        try:
            n = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
