#!/usr/bin/python3
"""
class base.
"""

class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else: 
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
