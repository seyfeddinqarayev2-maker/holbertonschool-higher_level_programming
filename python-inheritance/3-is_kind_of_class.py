#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance
of a class or an instance of a subclass of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or an instance
    of a class that inherited from a_class; otherwise False.
    """
    return isinstance(obj, a_class)


# Example usage
if __name__ == "__main__":
    class A:
        pass

    class B(A):
        pass

    a = A()
    b = B()

    print(is_kind_of_class(a, A))  # True
    print(is_kind_of_class(b, A))  # True, because B inherits from A
    print(is_kind_of_class(b, B))  # True
    print(is_kind_of_class(a, B))  # False
