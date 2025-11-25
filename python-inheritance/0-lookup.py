#!/usr/bin/python3
"""Function that returns a list of available attributes
and methods of an object"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
