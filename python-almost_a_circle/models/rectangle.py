#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): horizontal position.
            y (int): vertical position.
            id (int): identity of the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _check_integer(name, value):
        """Raise TypeError if value is not an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def _check_positive(self, name, value):
        """Check that value is an integer greater than 0."""
        self._check_integer(name, value)
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def _check_not_negative(self, name, value):
        """Check that value is an integer greater than or equal to 0."""
        self._check_integer(name, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self._check_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self._check_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        self._check_not_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        self._check_not_negative("y", value)
        self.__y = value
