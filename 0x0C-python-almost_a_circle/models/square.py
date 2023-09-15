#!/usr/bin/python3
""" Our square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Repr this square & inheritss from  Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Inits this Square.

        Args:
            size (int): size of this Square.
            x (int): x coordinate of this Square.
            y (int): y coordinate of this Square.
            id (int): square identity
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size of this Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ For updating this Square.

        Args:
            *args (ints): The new attr val.
                - 1st arg repr id attr
                - 2nd arg repr size attr
                - 3rd arg repr x attr
                - 4th arg repr y attr
            **kwargs (dict): The new key:val pairs of attr
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Dict repr of this Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ str( print() & str()) repr of this Square."""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
