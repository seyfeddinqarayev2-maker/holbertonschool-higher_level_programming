#!/usr/bin/python3
"""
Bu modul Square sinfini ehtiva edir,
Rectangle-dən miras alınır.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Kvadrat sinfi, Rectangle-dən miras alır"""

    def __init__(self, size):
        """Kvadratı size ilə yaradır"""
        self.integer_validator("size", size)
        self.__size = size
        # Kvadrat üçün width və height eyni olur
        super().__init__(size, size)

    def area(self):
        """Kvadratın sahəsini qaytarır"""
        return self.__size * self.__size
