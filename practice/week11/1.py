import pygame, sys, random, math

pygame.init()
clock = pygame.time.Clock()
Plane_size = 100
HEIGHT, WIDTH = (800, 800)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('HH')
fon = pygame.image.load('practice/week11/game1/Fon.png')
fon = pygame.transform.scale(fon, (HEIGHT, WIDTH))
meteorit = pygame.image.load('practice/week11/game1/Meteorit.png')
Hp_list = []

class Plane:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('practice/week11/game1/plane(1).png'), (Plane_size, Plane_size))
        self.rect = self.image.get_rect(center = (400, 400))
        self.angle = 0
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.angle += 1
        elif pressed[pygame.K_RIGHT]:
            self.angle -= 1
        return self.angle%36
    def draw(self):
        plane = pygame.transform.rotate(self.image, self.angle * 10)
        screen.blit(plane, self.rect)

class Point:
    def __init__(self, x, y, image, size, dx, dy):
        self.x = x
        self.y = y
        if dy < 0 and dx >= 0: self.image = pygame.transform.rotate(image, 90 - 57*(math.atan(dx/dy)))
        elif dy < 0 and dx < 0: self.image = pygame.transform.rotate(image, 180 + 57*(math.atan(dx/dy)))
        else: self.image = pygame.transform.rotate(image, 57*(math.atan(dx/dy)))
        self.size = size
        self.dx = dx
        self.dy = dy

class Ball:
    def __init__(self):
        self.size = random.randint(1, 3)*30
        self.image = pygame.transform.scale(pygame.image.load('practice/week11/game1/Meteorit.png'), (self.size, self.size))
        self.rect = self.image.get_rect()
        self.point = []
        self.speed = 10
        self.angle = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.bottom > 500):
            self.rect.top = 0
            self.speed += 0.1
            self.size = random.randint(1, 3)*30
            self.image = pygame.transform.scale(pygame.image.load('practice/week11/game1/Meteorit.png'), (self.size, self.size))
            x = random.randint(1, 3)
            x_or_y = random.randint(0, WIDTH//self.size - 1)
            self.dx = WIDTH//2 - x_or_y * self.size
            self.dy = HEIGHT//2
            if x == 3: self.point.append(Point(x_or_y*self.size, 0, self.image, self.size, self.dx, self.dy))
            elif x == 2: self.point.append(Point(0, x_or_y*self.size, self.image, self.size, self.dy, self.dx))
            else: self.point.append(Point(WIDTH, x_or_y*self.size, self.image, self.size, -self.dy, self.dx))
        return self.point
         
    def update(self):
        for points in self.point: 
            points.x += points.dx/100
            points.y += points.dy/100

    def draw(self):
        for points in self.point:
          screen.blit(points.image, (points.x, points.y))
          if abs(points.y - HEIGHT//2) < points.size and abs(points.x - WIDTH//2) < points.size:
                Hp_list.append(points.size//3)
                self.point.remove(points)
        return Hp_list

class point:
    def __init__(self, x, y, angle, dx, dy):
        self.x = x
        self.y = y
        self.angle = angle
        self.dx = dx
        self.dy = dy

class fire:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('practice/week11/game1/fireball.png'), (40, 40))
        self.Fire = []
        self.score = 0

    def move(self, angle):
        dx = math.sin(angle*10/57)
        dy = math.cos(angle*10/57)
        x = WIDTH//2 - 70 * dx 
        y = HEIGHT//2 - 70 * dy  
        self.Fire.append(point(x, y, angle, dx, dy))

    def draw(self):
        for points in self.Fire:
          points.x -= points.dx*10
          points.y -= points.dy*10
          screen.blit(self.image, (points.x, points.y))
          if points.x > WIDTH or points.x < 0: self.Fire.remove(points)
          elif points.y > HEIGHT or points.y < 0:  self.Fire.remove(points)
        screen.blit(
            pygame.font.SysFont('bahnschrift', 30).render('Your Score: {}'.format(self.score), True, BLUE),
            (50, 50)
        )

    def crash(self, balls):
        for points in self.Fire:
            for ball in balls:
                if abs(ball.x-points.x) < ball.size  and abs(ball.y-points.y) < ball.size:
                    self.score += ball.size//30
                    balls.remove(ball)
                    self.Fire.remove(points)
            
class Hp:
    def __init__(self):
        self.HP = 3
        self.percent = 100

    def move(self, HP_list):
        for percent in HP_list:
            self.percent -= percent
            if self.percent <= 0:
                self.HP -= 1
                if self.HP == 0:
                    game_over()
                self.percent = 100
        Hp_list.clear()
    def draw(self):
        pygame.draw.line(screen, RED, start_pos=(680, 710), end_pos=(680+self.percent, 710), width=30)
        msg = pygame.font.SysFont('bahnschrift', 16).render('HP: {}   percent: {}%'.format(self.HP, self.percent), True, GREEN)
        screen.blit(msg, (635, 700))

def game_over():
    while True:
        screen.fill(BLACK)
        msg = pygame.font.SysFont('bahnschrift', 40).render('Game Over', True, RED)
        screen.blit(msg, (300, 380))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

def main():
    runing = True
    angle, met_list = 0, []
    plane = Plane()
    ball = Ball()
    Fire = fire()
    HP = Hp()
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Fire.move(angle)
        screen.blit(fon, (0, 0))
        met_list = ball.move()
        HP_LIST = ball.draw()
        Fire.draw()
        Fire.crash(met_list)
        ball.update()
        angle = plane.update()
        plane.draw()
        HP.move(HP_LIST)
        HP.draw()
        pygame.display.update()
        clock.tick(30)
if __name__ == '__main__':
    main()

pygame.quit()  