#!/usr/bin/python3
"""
Bu modul Square sinfini ehtiva edir,
Rectangle-dən miras alır.
"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Kvadrat sinfi, Rectangle-dən miras alır"""

    def __init__(self, size):
        """Kvadratı size ilə yaradır"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Kvadratın sahəsini qaytarır"""
        return self.__size * self.__size

    def __str__(self):
        """Kvadratı [Square] <width>/<height> formatında string-ə"""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
