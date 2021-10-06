#!/usr/bin/python3
class LockedClass:
    """A locked class that prevents user from dynamically creating new instance
    attributes, except if it's first_name"""
    __slots__ = ['first_name']
