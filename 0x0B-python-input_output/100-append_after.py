#!/usr/bin/python3
"""Append str/txt after a given str."""


def append_after(filename="", search_string="", new_string=""):
    """Append/Insert text after each line having a given str in a file.

    Args:
        filename (str): name of file to append txt/str
        search_string (str): str to search for in this file.
        new_string (str): str to append/insert.
    """

    text = ""

    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
