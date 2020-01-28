#!/usr/bin/python3
"""
class base.
"""
import os
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inicialite class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json format"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        empty_list = []
        if list_objs:
            for i in list_objs:
                empty_list.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as filename:
            filename.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if cls.__name__ is "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ is "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        if not os.path.isfile(file)
            return []
        with open(file, "r") as filname:
            return [cls.create(**d) for d in cls.from_json_string(
                            filname.read())]
