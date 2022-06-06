#!/usr/bin/python3
'''
2. First Rectangle
class Rectangle that inherits from Base
'''


from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    Attriubetes inhereted:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initialization
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        get width
        '''
        return self.__width

    @property
    def height(self):
        '''
        get height
        '''
        return self.__height

    @property
    def x(self):
        '''
        get x
        '''
        return self.__x

    @property
    def y(self):
        '''
        get y
        '''
        return self.__y

    @width.setter
    def width(self, value):
        '''
        set width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        '''
        set height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        '''
        set x
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''
        set y
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Return area
        '''
        return self.__width * self.__height

    def display(self):
        '''
        print in stdout the Rectangle instance with
        the character # by taking care of x and y
        '''
        y = self.__y
        x = self.__x
        w = self.__width
        h = self.__height
        print("\n" * y + "\n".join(" " * x + "#" * w for i in range(h)))

    def __str__(self):
        '''
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height

        return f"[Rectangle] ({self.id}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        '''
        public method that assigns an argument to each attribute
        '''
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        '''
        public method that returns the dictionary representation of a Rectangle
        '''
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
