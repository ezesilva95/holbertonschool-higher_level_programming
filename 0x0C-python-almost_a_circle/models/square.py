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
        if args is not None:
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
                self.id = args[0]
            if "width" in kwargs:
                self.width = args[1]
            if "height" in kwargs:
                self.height = args[2]
            if "x" in kwargs:
                self.x = args[3]
            if "y" in kwargs:
                self.y = args[4]

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
