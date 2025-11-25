#!/usr/bin/python3
"""Bu modul Rectangle sinfini ehtiva edir"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Düzbucaqlı sinfi, BaseGeometry-dən miras alır"""

    def __init__(self, width, height):
        """Düzbucaqlını width və height ilə yaradır"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
