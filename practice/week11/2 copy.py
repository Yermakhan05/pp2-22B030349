import pygame, sys

pygame.init()
clock = pygame.time.Clock()

HEIGHT, WIDTH = (800, 800)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('')
screen.fill(WHITE)

class Button:
    def __init__(self):
        self.rect = pygame.transform.scale(pygame.image.load("paint/icons/rectangle.png"), (40, 40))
        self.circle = pygame.transform.scale(pygame.image.load("paint/icons/circle.png"), (40, 40))
        self.pen = pygame.transform.scale(pygame.image.load("paint/icons/pen.png"), (40, 40))
        self.rhomb = pygame.transform.scale(pygame.image.load("paint/icons/rhomb.png"), (40, 40))
        self.triangle = pygame.transform.scale(pygame.image.load("paint/icons/right-triangle.png"), (40, 40))
        self.rhombus = pygame.transform.scale(pygame.image.load("paint/icons/rhombus.png"), (40, 40))
        self.equilateral = pygame.transform.scale(pygame.image.load("paint/icons/equilateral-triangle.png"), (40, 40))
        self.eraser = pygame.transform.scale(pygame.image.load("paint/icons/eraser.png"), (40, 40))

    def draw(self):
        self.rect1 = screen.blit(self.pen, (260, 60))
        self.rect2 = screen.blit(self.circle, (300, 60))
        self.rect3 = screen.blit(self.rect, (340, 60))
        self.rect4 = screen.blit(self.triangle, (380, 60))
        self.rect5 = screen.blit(self.rhomb, (420, 60))
        self.rect6 = screen.blit(self.equilateral, (460, 60))
        self.rect7 = screen.blit(self.rhombus, (500, 60))
        self.color1 = pygame.draw.rect(screen, RED, (60, 100, 40, 40))
        self.color2 = pygame.draw.rect(screen, BLUE, (60, 140, 40, 40))
        self.color3 = pygame.draw.rect(screen, GREEN, (60, 180, 40, 40))
        self.color4 = pygame.draw.rect(screen, BLACK, (60, 220, 40, 40))
        self.color5 = screen.blit(self.eraser, (60, 260))
class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self):
        raise NotImplementedError

class Pen(GameObject):
    def __init__(self, color, *args, **kwargs):
        self.line = []
        self.color = color
        if color == 'white': self.width = 100
        else: self.width = 5

    def draw(self):
        for idx, point in enumerate(self.line[:-1]):
            pygame.draw.line(screen, self.color, start_pos=point, end_pos=self.line[idx+1], width=self.width)

    def update(self, mouse_pos):
        self.line.append(mouse_pos)

def main():
    runing = True
    active_obj = None
    button = Button()
    current_shape = 'pen'
    color = 'black'
    objects = []
    while runing:
        for obj in objects:
            obj.draw()
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect1.collidepoint(pygame.mouse.get_pos()): current_shape = 'pen'
            if button.color1.collidepoint(pygame.mouse.get_pos()): color = 'red'
            elif button.color2.collidepoint(pygame.mouse.get_pos()): color = 'blue'
            elif button.color3.collidepoint(pygame.mouse.get_pos()): color = 'green'
            elif button.color4.collidepoint(pygame.mouse.get_pos()): color = 'black'
            elif button.color5.collidepoint(pygame.mouse.get_pos()): color = 'white'
            else:
                if current_shape == 'pen':
                    active_obj = Pen(color, colorstart_pos=event.pos)
        if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
            active_obj.draw()
            objects.append(active_obj)
            active_obj = None
        if event.type == pygame.MOUSEMOTION and active_obj is not None:
            active_obj.draw()
            active_obj.update(mouse_pos = pygame.mouse.get_pos())
        button.draw()
        pygame.display.flip()
        clock.tick(90)
if __name__ == '__main__':
    main()

pygame.quit()