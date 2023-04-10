import pygame

WIDTH, HEIGHT = 800, 800
class Button:
    def __init__(self, screen):
        self.screen = screen

        self.rect_icon = pygame.transform.scale(pygame.image.load('icons/rectangle.png'), (40, 40))
        self.rect2_icon = pygame.transform.scale(pygame.image.load('icons/pen.png'), (40, 40))
        self.rect3_icon = pygame.transform.scale(pygame.image.load('icons/circle.png'), (40, 40))
        self.rect4_icon = pygame.transform.scale(pygame.image.load('icons/right-triangle.png'), (40, 40))
        self.rect5_icon = pygame.transform.scale(pygame.image.load('icons/equilateral-triangle.png'), (40, 40))
        self.rect6_icon = pygame.transform.scale(pygame.image.load('icons/rhomb.png'), (40, 40))
        self.eraser_icon = pygame.transform.scale(pygame.image.load('icons/eraser.png'), (20, 20))

    def draw(self):
        #Tools
        self.rect = self.screen.blit(
            self.rect_icon,
            (WIDTH // 2, 20)
        )
        self.rect2 = self.screen.blit(
            self.rect2_icon,
            (WIDTH // 2 - 40, 20)
        )
        self.rect3 = self.screen.blit(
            self.rect3_icon,
            (WIDTH // 2 + 40, 20)
        )
        self.rect4 = self.screen.blit(
            self.rect4_icon,
            (WIDTH // 2 + 80, 20)
        )
        self.rect5 = self.screen.blit(
            self.rect5_icon,
            (WIDTH // 2 + 120, 20)
        )
        self.rect6 = self.screen.blit(
            self.rect6_icon,
            (WIDTH // 2 + 160, 20)
        )


        #Colors
        self.switch_to_red = pygame.draw.rect(
            self.screen,
            'red',
            (0, 0, 20, 20)
        )
        self.switch_to_blue = pygame.draw.rect(
            self.screen,
            'blue',
            (0, 20, 20, 20)
        )
        self.switch_to_green = pygame.draw.rect(
            self.screen,
            'green',
            (0, 40, 20, 20)
        )
        self.switch_to_black = pygame.draw.rect(
            self.screen,
            'black',
            (0, 60, 20, 20)
        )
        self.eraser_rect = self.screen.blit(
            self.eraser_icon,
            (0, 80)
        )