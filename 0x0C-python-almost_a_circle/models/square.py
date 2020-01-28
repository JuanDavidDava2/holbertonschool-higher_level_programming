#!/usr/bin/python3
"""
class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """property"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """return str"""
        return("[Square] ({}) {}/{} - {}"
               .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """update"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.size = j
            elif i == 2:
                self.x = j
            elif i == 3:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary"""
        to_dic = {}
        to_dic["id"] = self.id
        to_dic["size"] = self.size
        to_dic["x"] = self.x
        to_dic["y"] = self.y
        return to_dic
