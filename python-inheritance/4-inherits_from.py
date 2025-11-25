#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance
of a class that inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited from
    a_class (directly or indirectly), but not if obj is exactly a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class


# Example usage
if __name__ == "__main__":
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    a = A()
    b = B()
    c = C()

    print(inherits_from(a, A))  # False, a is exactly A
    print(inherits_from(b, A))  # True, B inherits from A
    print(inherits_from(c, A))  # True, C inherits from B -> A
    print(inherits_from(c, B))  # True, C inherits from B
    print(inherits_from(b, B))  # False, b is exactly B
