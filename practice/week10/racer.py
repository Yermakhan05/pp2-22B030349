import pygame, sys

pygame.init()
clock = pygame.time.Clock()

HEIGHT, WIDTH = 400, 600
SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('RACER GAME')


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class RED:
    def __init__(self):
        self.cars = []

class BLUE:
    def __init__(self):
        self.x = 100
        self.image = pygame.transform.scale(
            pygame.image.load('tsis8/images/BLUE_car.png'), 
            (100, 120)
        )
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.x += 10
            if self.x > 300:
                self.x = 300
        elif pressed[pygame.K_LEFT]:
            self.x -= 10
            if self.x < 0:
                self.x = 0
        
    def draw(self):
        SCREEN.blit(self.image, (self.x, 460))


def main():
    runing = True
    dx = 0
    blue_car = BLUE()
    while runing:
        SCREEN.fill((255, 255, 255))
        # SCREEN.blit(blue_car.image, (blue_car.x, 470))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
        blue_car.update()
        blue_car.draw()
        pygame.display.update()
        clock.tick(60)
        

if __name__ == '__main__':
    main()
pygame.quit() 