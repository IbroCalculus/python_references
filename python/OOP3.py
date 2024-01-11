
#Super Keyword

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

        '''
        INSTEAD OF:
        self.length = length
        self.width = width
        '''
    def area(self):
        theArea = self.width * self.length
        print(f'The area of the square = {theArea}')

        # print(f'AREA OF SQUARE = {self.width * self.length}')


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

        '''
        INSTEAD OF:
        self.length = length
        self.width = width
        self.height = height
        '''
    def volume(self):
        print(f'VOLUME OF CUBE = {self.width * self.length * self.height}')