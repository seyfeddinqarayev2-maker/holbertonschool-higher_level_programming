#!/usr/bin/python3

def uppercase(str):
    for c in str:
        # Kiçik hərfdirsə böyük hərfə çevir, yoxsa olduğu kimi çap et
        print("{}".format(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c), end="")
    print()
