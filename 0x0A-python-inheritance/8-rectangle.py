#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A representation of a rectangle"""
    def __int__(self, width, height):
        """instantiation of rectangle"""
        self.interger_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
