#!/usr/bin/python
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for sorted_keys in keys:
        print("{}: {}".format(sorted_keys, a_dictionary[sorted_keys]))
