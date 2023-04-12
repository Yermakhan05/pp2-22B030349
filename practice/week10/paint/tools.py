import pygame
from math import *

class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self):
        raise NotImplementedError

class Pen(GameObject):
    def __init__(self, color, screen, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]
        self.color = color
        self.screen = screen
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                self.screen,
                self.color,
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=5,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)

class Eraser(GameObject):
    def __init__(self, screen, *args, **kwargs):
        self.points = []
        self.screen = screen
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                self.screen,
                'white',
                start_pos=point,
                end_pos=self.points[idx + 1],
                width=100,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)

class Circle(GameObject):
    def __init__(self, color, screen, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.screen = screen

    def draw(self):
        circle_center = self.start_pos
        Radius = (sqrt((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2))

        pygame.draw.circle(
            self.screen,
            self.color,
            (self.start_pos[0], self.start_pos[1]),
            Radius,
            width = 5
        )
    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class RightTriangle(GameObject):
    def __init__(self, color, screen, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        self.screen = screen

    def draw(self):
        x = max(self.start_pos[0], self.end_pos[0])
        y = max(self.start_pos[1], self.end_pos[1])
        x0 = min(self.start_pos[0], self.end_pos[0])
        y0 = min(self.start_pos[1], self.end_pos[1])

        r = sqrt((x-x0)**2 + (y-y0)**2)

        leftx = -((r/2)+x0)
        lefty = -(((3)**0.5)*r)/2 + y0

        rx = ((r / 2) + x0)
        ry = (((3) ** 0.5) * r) / 2 + y0

        pygame.draw.polygon(
            self.screen,
            self.color,
            ((x0, y0), (rx, ry), (leftx, lefty)),
            width=5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Rectangle(GameObject):
    def __init__(self, color,screen, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        self.screen = screen

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            self.screen,
            self.color,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class EquilateralTriangle(GameObject):
    def __init__(self, color, screen, start_pos):
        self.screen = screen
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        Distance = (sqrt((self.end_pos[1] - self.start_pos[1]) ** 2 + (self.end_pos[0] - self.start_pos[0]) ** 2))
        a = Distance * sqrt(3)

        x = self.end_pos[0]
        y = self.end_pos[1]

        pygame.draw.polygon(
            self.screen,
            self.color,
            ((x, y), (x - a/2, y - sqrt(3)/2*a), (x + a/2, y + sqrt(3)/2*a))
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

    def draw(self):
        pass

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos