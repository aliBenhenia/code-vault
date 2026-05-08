import sys
from ft_filter import ft_filter


def main():
    """
    Takes a string S and integer N as arguments.
    Prints words from S whose length is greater than N.
    Raises AssertionError if arguments are invalid.
    """
    try:
        args = sys.argv[1:]
        assert len(args) == 2, "the arguments are bad"
        try:
            n = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")
        if args[0].lstrip('-').isdigit():
            raise AssertionError("the arguments are bad")
        s = args[0]
        result = list(ft_filter(lambda w: len(w) > n, s.split(' ')))
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
