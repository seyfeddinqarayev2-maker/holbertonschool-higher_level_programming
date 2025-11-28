#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization support."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name,
        and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in this list are
        retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with those in
        json.

        json is assumed to be a dictionary where keys are attribute names
        and values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
