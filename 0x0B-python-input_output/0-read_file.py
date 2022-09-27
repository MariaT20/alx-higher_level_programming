#!/usr/bin/python3
"""
A module that reads a text file
"""


def read_file(filename=""):
    """
     reads the the text file (UTF8) and prints it to stdout
     Returns none
     """
    with open(filename, "r", encoding="utf-8") as fn:
        print(fn.read(), end="")
