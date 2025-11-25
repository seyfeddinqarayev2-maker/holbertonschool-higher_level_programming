#!/usr/bin/python3
"""
Bu modul Square sinfini ehtiva edir,
Rectangle-dən miras alır.
"""

Rectangle = __import__('11-rectangle').Rectangle


class Square(Rectangle):
    """Kvadrat sinfi, Rectangle-dən miras alır"""

    def __init__(self, size):
        """Kvadratı size ilə yaradır"""
        self.integer_validator("size", size)
        self.__size = size
        # Kvadrat olduğu üçün width və height eyni olur
        super().__init__(size, size)

    def area(self):
        """Kvadratın sahəsini qaytarır"""
        return self.__size * self.__size

    def __str__(self):
        """Kvadratı [Square] <width>/<height> formatında string-ə çevirir"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
