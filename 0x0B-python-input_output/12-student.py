#!/usr/bin/python3
"""
class Student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            dirt = {}
            for item in attrs:
                if hasattr(self, item):
                    dirt[item] = getattr(self, item)
            return dirt
