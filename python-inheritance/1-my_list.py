#!/usr/bin/python3
"""
Module that defines the MyList class.
This class inherits from list and adds a method to print a sorted version.
"""


class MyList(list):
    """
    MyList class that inherits from built-in list.
    Provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        Does not modify the original list.
        Returns the sorted list.
        """
        print(sorted(self))
