#!/usr/bin/python3
"""
Reactangle class
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor funtion"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property funtion"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter funtion"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property funtion"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter funtion"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property funtion"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter funtion"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property funtion"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter funtion"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """print rectangle"""
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """show str funtion"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ubdate funtion"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.width = j
            elif i == 2:
                self.height = j
            elif i == 3:
                self.x = j
            elif i == 4:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        elif "width" in kwargs:
            self.width = kwargs["width"]
        elif "height" in kwargs:
            self.height = kwargs["height"]
        elif "x" in kwargs:
            self.x = kwargs["x"]
        elif "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary funtion"""
        to_dic = {}
        to_dic["id"] = self.id
        to_dic["width"] = self.width
        to_dic["height"] = self.height
        to_dic["x"] = self.x
        to_dic["y"] = self.y
        return to_dic
