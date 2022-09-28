#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds key/value in a dictionary

    Args:
        a_dictionary (dictionary)
        key (string) : string
        value (any)
    """
    a_dictionary[key] = value
    return (a_dictionary)
