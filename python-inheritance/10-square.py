#!/usr/bin/python3

# Düzgün import
Rectangle = __import__('8-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
