import sys

import pygame
from math import *
from tools import *
from Button import Button

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
clock = pygame.time.Clock()

def main():
    active_obj = None
    button = Button(SCREEN)
    objects = [
        button
    ]

    current_shape = 'pen'
    color = 'black'
    while True:
        SCREEN.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'rectangle'
                if button.rect2.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'pen'
                if button.rect3.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'circle'
                if button.rect4.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'righttriangle'
                if button.rect5.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'equilateraltriangle'

                if button.switch_to_red.collidepoint(pygame.mouse.get_pos()):
                    color = 'red'
                if button.switch_to_blue.collidepoint(pygame.mouse.get_pos()):
                    color = 'blue'
                if button.switch_to_green.collidepoint(pygame.mouse.get_pos()):
                    color = 'green'
                if button.switch_to_black.collidepoint(pygame.mouse.get_pos()):
                    color = 'black'
                if button.eraser_rect.collidepoint(pygame.mouse.get_pos()):
                    color = 'white'
                    current_shape = 'eraser'

                else:
                    if current_shape == 'pen':
                        active_obj = Pen(color, SCREEN, colorstart_pos=event.pos)
                    elif current_shape == 'rectangle':
                        active_obj = Rectangle(color, SCREEN, start_pos=event.pos)
                    elif current_shape == 'circle':
                        active_obj = Circle(color, SCREEN, start_pos=event.pos)
                    elif current_shape == 'righttriangle':
                        active_obj = RightTriangle(color, SCREEN, start_pos=event.pos)
                    elif current_shape == 'equilateraltriangle':
                        active_obj = EquilateralTriangle(color, SCREEN, start_pos=event.pos)

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        for obj in objects:
            obj.draw()

        clock.tick(90)
        pygame.display.flip()


if __name__ == '__main__':
    main()