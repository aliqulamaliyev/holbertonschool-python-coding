#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with the private size attribute."""
        self.size = size  # This will call the setter for validation

    @property
    def size(self):
        """Retrieve the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size value with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

