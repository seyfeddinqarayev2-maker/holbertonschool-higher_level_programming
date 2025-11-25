#!/usr/bin/python3
"""Defines a BaseGeometry class with integer validation."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise an Exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
