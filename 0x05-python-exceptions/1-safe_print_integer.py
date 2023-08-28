#!/usr/bin/python3

"""Print an int using "{:d}".format().

    Args:
        value (int):  int to print.

    Returns:
        0 if( TypeError|ValueError) else 1
    """


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
