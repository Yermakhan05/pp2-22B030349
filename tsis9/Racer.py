import pygame, sys, random, time

pygame.init()
clock = pygame.time.Clock()

HEIGHT, WIDTH = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RACER GAME')

street = pygame.image.load('tsis8/images/Street.png')
pygame.mixer.Sound('tsis9/music/background.wav').play(-1)

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

class Coin:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('tsis9/images/coin.png'), (50, 50))
        self.x = random.randint(0, WIDTH-50)
        self.y = random.randint(50, HEIGHT-150)

    def move(self):
        self.x = random.randint(0, WIDTH-50)
        self.y = 0
        x = random.randint(1, 3)
        if x == 2: 
            self.image = pygame.transform.scale(pygame.image.load('tsis9/images/coin.png'), (50, 50))
            Score = 1
        else: 
            self.image = pygame.transform.scale(pygame.image.load('tsis9/images/money.png'), (50, 50))
            Score = 2
        return Score
    def draw(self):
        self.y += 5
        SCREEN.blit(self.image, (self.x, self.y))
    def Check(self, x, y):
        if self.y >= 550: return True
        if abs(self.x - x) < 50:
            if abs(self.y - y) < 50:
                return True
        return False


class Red:
    def __init__(self):
        self.Score = 1
        self.image = pygame.transform.scale(
            pygame.image.load('tsis8/images/RED_car.png'), 
            (100, 120)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width//2, WIDTH - self.rect.width), 0)

    def replay_car(self, speed):
        if speed > 20:
            speed = 20
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            self.Score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width//2, WIDTH - self.rect.width), 0)
        return speed

    def Point(self):
        score = pygame.font.SysFont("arial", 35).render("You Score: "+str(self.Score),True, RED)
        SCREEN.blit(score, (10, 10))

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def game_over(self, x_r, y_r):
        x = self.rect[0]
        y = self.rect[1]
        if abs(y - y_r)< 120:
            if abs(x-x_r) < 50:
                return True
        return False
        
class Blue:
    def __init__(self):
        self.x = 100
        self.y = 460
        self.angle = 0
        self.image = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('tsis8/images/BLUE_car.png'), 
            (100, 120)
        ), self.angle)
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.angle = -5
            self.x += 10
            if self.x > 300: self.x = 300
        elif pressed[pygame.K_LEFT]:
            self.angle = 5
            self.x -= 10
            if self.x < 0: self.x = 0
        else: self.angle = 0
        self.image = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('tsis8/images/BLUE_car.png'), 
            (100, 120)
        ), self.angle)
        return self.x, self.y
        
    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))


def main():
    runing = True
    speed = 5
    coin = Coin()
    Y = 0
    blue_car = Blue()
    Event = pygame.USEREVENT + 1
    tt = pygame.time.set_timer(Event, 1000)
    red_car = Red()
    while runing:
        SCREEN.blit(street, (0, Y))
        SCREEN.blit(street, (0, Y-600))
        Y += speed
        if Y >= 600: Y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            if event.type == tt:
                sec += 1 
        
        x, y = blue_car.update()
        blue_car.draw()
        red_car.draw()
        if coin.Check(x, y):
            Score = coin.move()
            speed += Score
        coin.draw()
        red_car.Point()
        speed = red_car.replay_car(speed)
        if red_car.game_over(x, y):
            pygame.mixer.stop() 
            pygame.mixer.Sound('tsis9/music/crash.wav').play()
            game_over(True)
        pygame.display.update()
        clock.tick(60)
        

if __name__ == '__main__':
    main()
pygame.quit()