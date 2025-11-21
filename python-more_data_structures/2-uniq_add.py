#!/usr/bin/python3def uniq_add(my_list=[]):
    unique_items = []
    total = 0

    for n in my_list:
        if n not in unique_items:
            unique_items.append(n)
            total += n

    return total
