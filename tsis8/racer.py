import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

HEIGHT, WIDTH = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RACER GAME')

street = pygame.image.load('tsis8/images/Street.png')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def game_over(run):
    while run:
            SCREEN.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return main()
                    elif event.key == pygame.K_q:
                        sys.exit()
            pygame.display.update()

class Red:
    def __init__(self):
        self.Score = 1
        self.image = pygame.transform.scale(
            pygame.image.load('tsis8/images/RED_car.png'), 
            (100, 120)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width//2, WIDTH - self.rect.width), 0)

    def replay_car(self):
        speed = self.Score + 2
        if speed > 10:
            speed = 10
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            self.Score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width//2, WIDTH - self.rect.width), 0)

    def Point(self):
        score = pygame.font.SysFont("arial", 35).render("You Score: "+str(self.Score),True, RED)
        SCREEN.blit(score, (10, 10))

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def game_over(self, x_r):
        x = self.rect[0]
        y = self.rect[1]
        if y >= 340:
            if abs(x-x_r) < 50:
                return True
        return False
        


class Blue:
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
                game_over(True)
        elif pressed[pygame.K_LEFT]:
            self.x -= 10
            if self.x < 0:
                game_over(True)
        return self.x
        
    def draw(self):
        SCREEN.blit(self.image, (self.x, 460))


def main():
    runing = True
    dx = 0
    blue_car = Blue()
    red_car = Red()
    while runing:
        SCREEN.blit(street, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
        x = blue_car.update()
        blue_car.draw()
        red_car.draw()
        red_car.Point()
        red_car.replay_car()
        if red_car.game_over(x): game_over(True)
        pygame.display.update()
        clock.tick(60)
        

if __name__ == '__main__':
    main()
pygame.quit() 