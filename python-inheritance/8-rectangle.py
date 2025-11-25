#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """BaseGeometry-dən miras alan Düzbucaqlı sinfi"""

    def __init__(self, en, uzunluq):
        """Düzbucaqlını en və uzunluq ilə yaradır"""
        # En və uzunluğu yoxlayır ki, müsbət tam ədəd olsun
        self.integer_validator("en", en)
        self.integer_validator("uzunluq", uzunluq)
        # Özəl atributlar
        self.__en = en
        self.__uzunluq = uzunluq
