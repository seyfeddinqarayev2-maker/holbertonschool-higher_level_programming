#!/usr/bin/python3
"""Module that returns a dictionary description of a class instance
for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
of an object."""
    return obj.__dict__
