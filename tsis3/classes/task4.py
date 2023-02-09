import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def show(self):
        print(self.x, self.y)

    def dist(self, self1):
        print(math.sqrt((self1.x - self.x) ** 2 + (self1.y - self.y) ** 2))

x0 = int(input("x0 = "))
y0 = int(input("y0 = "))
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
dx = int(input("dx = "))
dy = int(input("dy = "))

answer = Point(x0, y0)
answer1 = Point(x1, y1)
answer.move(dx, dy)
answer.show()
answer.dist(answer1)