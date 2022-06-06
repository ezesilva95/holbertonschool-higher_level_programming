#!/usr/bin/python3
'''
10. And now, the Square!
class Square that inherits from Rectangle
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Square that inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialization
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''
        get width
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        set size
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        return [Square] (<id>) <x>/<y> - <size>
        '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        '''
        public method def update(self, *args, **kwargs) that assigns attributes
        '''
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
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
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
