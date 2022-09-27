#!/usr/bin/python3
"""
A mmodule that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as fn:
        for char in text:
            fn.write(char)
            return len(text)
