#!/usr/bin/python3
""" Creates/defines a func tat prints a square """


def print_square(size):
    """
    Print square having a # char.
    Args:
        size (int): height/width of our square.
    Raises:
        TypeError: where/when size is not an int.
        ValueError: when/where size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
