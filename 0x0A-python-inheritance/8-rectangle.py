#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry

class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __inti__(self, width, height):
        """Instantation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height