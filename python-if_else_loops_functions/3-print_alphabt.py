#!/usr/bin/python3
for c in range(97, 123):
    if c != 101 and c != 113:  # ASCII kodları: e=101, q=113
        print("{}".format(chr(c)), end="")
