#!/usr/bin/python3
"""Module that defines a function to append text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file and returns chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
