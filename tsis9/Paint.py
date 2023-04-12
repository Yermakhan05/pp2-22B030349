import pygame, sys, math

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
        self.rect = pygame.transform.scale(pygame.image.load("tsis9/images/rectangle.png"), (40, 40))
        self.circle = pygame.transform.scale(pygame.image.load("tsis9/images/circle.png"), (40, 40))
        self.pen = pygame.transform.scale(pygame.image.load("tsis9/images/pen.png"), (40, 40))
        self.rhomb = pygame.transform.scale(pygame.image.load("tsis9/images/rhomb.png"), (40, 40))
        self.triangle = pygame.transform.scale(pygame.image.load("tsis9/images/right-triangle.png"), (40, 40))
        self.rhombus = pygame.transform.scale(pygame.image.load("tsis9/images/rhombus.png"), (40, 40))
        self.equilateral = pygame.transform.scale(pygame.image.load("tsis9/images/equilateral-triangle.png"), (40, 40))
        self.eraser = pygame.transform.scale(pygame.image.load("tsis9/images/eraser.png"), (40, 40))

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

    def update(self, mouse_pos, objects):
        for obj in objects:
           obj.draw()
        self.line.append(mouse_pos)
        # screen.fill(WHITE)
class Circle(GameObject):
    def __init__(self, color, start_pos):
        self.center = start_pos
        self.color = color
        self.end_pos = start_pos
    def draw(self):
        Radius = math.sqrt(abs(self.end_pos[0]-self.center[0])**2 + abs(self.end_pos[1]-self.center[1])**2)
        pygame.draw.circle(screen, self.color, (self.center[0], self.center[1]), Radius, width=5)
    
    def update(self, mouse_pos, objects):
        screen.fill(WHITE)
        self.end_pos = mouse_pos
        for obj in objects:
            obj.draw()

class Rect(GameObject):
    def __init__(self, color, start_pos, shape):
        self.start_pos = start_pos
        self.color = color
        self.end_pos = start_pos
        self.rect = shape
    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])
        height = end_pos_y - start_pos_y
        width = end_pos_x - start_pos_x
        x = max(height, width)
        if self.rect == 'square':
            pygame.draw.rect(screen, self.color, (start_pos_x, start_pos_y, x, x), width=5)
        else: 
            pygame.draw.rect(screen, self.color, (start_pos_x, start_pos_y, width, height), width=5)
    def update(self, mouse_pos, objects):
        screen.fill(WHITE)
        self.end_pos = mouse_pos
        for obj in objects:
            obj.draw()

class R_triangle(GameObject):
    def __init__(self, color, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(screen, self.color, [(start_pos_x, start_pos_y), (end_pos_x, end_pos_y), (start_pos_x, end_pos_y)], width=5)
    def update(self, mouse_pos, objects):
        screen.fill(WHITE)
        self.end_pos = mouse_pos
        for obj in objects:
            obj.draw()

class E_triangle(GameObject):
    def __init__(self, color, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])
        dx = (end_pos_x - start_pos_x)
        pygame.draw.polygon(screen, self.color, [(start_pos_x, end_pos_y), (end_pos_x, start_pos_y), (end_pos_x+dx, end_pos_y)], width=5)
    
    def update(self, mouse_pos, objects):
        screen.fill(WHITE)
        self.end_pos = mouse_pos
        for obj in objects:
            obj.draw()
    
class Rhombus(GameObject):
    def __init__(self, color, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])
        dx = end_pos_x - start_pos_x
        dy = end_pos_y - start_pos_y
        pygame.draw.polygon(
            screen, 
            self.color, 
            [(start_pos_x, end_pos_y), (end_pos_x, start_pos_y), (end_pos_x+dx, end_pos_y), (end_pos_x, end_pos_y+dy)], 
            width=5)
    
    def update(self, mouse_pos, objects):
        screen.fill(WHITE)
        self.end_pos = mouse_pos
        for obj in objects:
            obj.draw()
    

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect1.collidepoint(pygame.mouse.get_pos()): current_shape = 'pen'
                elif button.rect2.collidepoint(pygame.mouse.get_pos()): current_shape = 'circle'
                elif button.rect3.collidepoint(pygame.mouse.get_pos()): current_shape = 'rect'
                elif button.rect4.collidepoint(pygame.mouse.get_pos()): current_shape = 'r_triangle'
                elif button.rect6.collidepoint(pygame.mouse.get_pos()): current_shape = 'e_triangle'
                elif button.rect7.collidepoint(pygame.mouse.get_pos()): current_shape = 'rhombus'
                elif button.rect5.collidepoint(pygame.mouse.get_pos()): current_shape = 'square'

                if button.color1.collidepoint(pygame.mouse.get_pos()): color = 'red'
                elif button.color2.collidepoint(pygame.mouse.get_pos()): color = 'blue'
                elif button.color3.collidepoint(pygame.mouse.get_pos()): color = 'green'
                elif button.color4.collidepoint(pygame.mouse.get_pos()): color = 'black'
                elif button.color5.collidepoint(pygame.mouse.get_pos()): color = 'white'
                else:
                    if current_shape == 'pen': active_obj = Pen(color, colorstart_pos=event.pos)
                    elif current_shape == 'circle': active_obj = Circle(color, event.pos)
                    elif current_shape == 'rect': active_obj = Rect(color, event.pos, current_shape)
                    elif current_shape == 'square': active_obj = Rect(color, event.pos, current_shape)
                    elif current_shape == 'r_triangle': active_obj = R_triangle(color, event.pos)
                    elif current_shape == 'e_triangle': active_obj = E_triangle(color, event.pos)
                    elif current_shape == 'rhombus': active_obj = Rhombus(color, event.pos)
            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.update(mouse_pos = pygame.mouse.get_pos(), objects = objects)
                active_obj.draw()
                    
            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None
        button.draw()
        pygame.display.flip()
        clock.tick(90)
if __name__ == '__main__':
    main()

pygame.quit()