#!/usr/bin/python3
"""
Bu modul Square sinfini ehtiva edir,
Rectangle-dən miras alır.
"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Kvadrat sinfi, Rectangle-dən miras alır"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self._Rect__width, self._Rect__height)
