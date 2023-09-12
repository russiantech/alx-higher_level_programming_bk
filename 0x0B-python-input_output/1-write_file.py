#!/usr/bin/python3
"""Write A Text Into A File"""


def write_file(filename="", text=""):
    """Write str to a text file(utf-8).

    Args:
        filename (str): name of file
        text (str): text to write to this  file.
    Returns:
         num of chars written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
