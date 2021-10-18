#!/usr/bin/python3
"""
This module contains the "Base" class
"""


import csv
import json
import turtle


class Base:
    """A Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
