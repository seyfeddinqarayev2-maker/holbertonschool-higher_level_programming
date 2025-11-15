#!/usr/bin/python3
def islower(c):
    """Check if character is lowercase"""
    if len(c) != 1:
        return False
    return ord('a') <= ord(c) <= ord('z')
