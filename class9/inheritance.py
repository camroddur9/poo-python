class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':
    rectangle = Rectangle(3, 4)
    print(rectangle.area())
    square = Square(5)
    print(square.area())