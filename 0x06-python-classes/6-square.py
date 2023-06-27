#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Initialize the Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        @property
        def position(self):
            return (self.__position)

        @position.setter
        def position(self, value):
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value


        def area(self):
            return (self.__size * self.__size)
