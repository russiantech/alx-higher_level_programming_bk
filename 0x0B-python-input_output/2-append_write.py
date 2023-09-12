#!/usr/bin/python3
"""Add Some more text @ the end of a file"""


def append_write(filename="", text=""):
    """Appends text to filename.

    Args:
        filename (str): name of file to append text.
        text (str): str to append to filename
    Returns:
        num of chars appended.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
