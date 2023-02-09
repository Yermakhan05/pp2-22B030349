class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.lenth = length
        self.width = width

    def area(self):
        return self.lenth * self.width

lenth, width = input().split()
lenth = int(lenth)
width = int(width)
answer = Rectangle(lenth, width)

print(answer.area())