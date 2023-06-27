#!/usr/bin/python3

"""Defining a square class"""


class Square:
    """initializing the square class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
