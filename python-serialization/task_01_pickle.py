#!/usr/bin/python3
"""Module for pickling and unpickling a custom class using the pickle module."""

import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a pickle file.

        Args:
            filename (str): The name of the pickle file.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except (OSError, pickle.PickleError):
            return None
