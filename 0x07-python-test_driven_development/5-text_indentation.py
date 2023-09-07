#!/usr/bin/python3
""" text indentation function."""


def text_indentation(text):
    """will print-text having 2 \n  after each '.', '?', and ':'.

    Args:
        text (str): Text str to print.
    Raises:
        TypeError:when text is'nt a str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
