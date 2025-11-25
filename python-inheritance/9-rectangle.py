#!/usr/bin/python3
"""BaseGeometry-dən miras alınır"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Düzbucaqlı sinfi, BaseGeometry-dən miras alır"""

    def __init__(self, width, height):
        """Düzbucaqlını width və height ilə yaradır"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Düzbucaqlının sahəsini qaytarır"""
        return self.__width * self.__height

    def __str__(self):
        """Düzbucaqlını istədiyimiz formatda string-ə çevirir"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
