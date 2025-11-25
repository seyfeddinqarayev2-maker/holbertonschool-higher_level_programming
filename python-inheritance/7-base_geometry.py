#!/usr/bin/python3
"""Defines a BaseGeometry class with area and integer validation."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Public instance method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
