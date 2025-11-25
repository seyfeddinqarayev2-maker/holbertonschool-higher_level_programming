#!/usr/bin/python3
"""
Module that defines the is_same_class function.
Checks if an object is exactly an instance of a given class.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, otherwise False."""
    return type(obj) == a_class


# Example usage
if __name__ == "__main__":
    class A:
        pass

    class B(A):
        pass

    a = A()
    b = B()

    print(is_same_class(a, A))  # True
    print(is_same_class(b, A))  # False
    print(is_same_class(b, B))  # True

