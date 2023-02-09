class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenth):
        super().__init__()
        self.lenth = lenth

    def area(self):
        return self.lenth * self.lenth

lenth = int(input())
answer = Square(lenth)

print(answer.area())