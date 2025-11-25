#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Public instance method that raises an exception."""
        raise Exception("area() is not implemented")
