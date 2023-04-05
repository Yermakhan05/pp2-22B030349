import pygame
import random


File = open("Score.txt", 'r')
s = int(File.read())

pygame.init()
clock = pygame.time.Clock()
HEIGHT, WIDTH = 800, 800
BLOCK = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption('Asteroid')
Menu = pygame.image.load("practice/week10/materials/MENU.png")
Menu = pygame.transform.scale(Menu, (HEIGHT, WIDTH))
fon = pygame.image.load("practice/week10/materials/Fon.png")
fon = pygame.transform.scale(fon, (HEIGHT, WIDTH))
def highScore(s):
    runing = True
    while runing:
        screen.fill((0, 0, 0))
        message(s, WHITE, (380, 380), 40)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return True
        pygame.display.flip()
def menu(run):
    while run:
            screen.blit(Menu, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
                    if event.key == pygame.K_s:
                        run = highScore(str(s))
                    elif event.key == pygame.K_q:
                        return False
            pygame.display.update()

def rotate_plane(angle):
    Plane = pygame.image.load("practice/week10/materials/plane.png")
    Plane = pygame.transform.scale(Plane, (50, 50))
    return pygame.transform.rotate(Plane, angle)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Asteriod:
    def __init__(self):
        self.asteriod = []
        self.point = 0
    def Score(self, point):
        score = pygame.font.SysFont("arial", 35).render("You Score: "+str(point),True, RED)
        screen.blit(score, (10, 10))
        return self.point
    def Points(self):
        x, y = random.randint(0, WIDTH//50 - 1), 0
        self.point += 1
        self.asteriod.append(Point(x, y))
    def draw(self):
        for point in self.asteriod:
            if point.y > HEIGHT-50: self.asteriod.remove(point)
            metor_draw(point.x*50, point.y)
            point.y += 50
            
    def HP(self, hp):
        pygame.draw.line(screen, GREEN, start_pos=(700, 720), end_pos=(700+hp*20, 720), width=15)
        msg = pygame.font.SysFont("arial", 30).render("HP: {}".format(hp), True, BLUE)
        screen.blit(msg, (640, 700))
    def game_over(self, x, y):
        for point in self.asteriod:
            if abs(point.x*50 - x) < 20:
                if abs(point.y - y)< 20:
                    return False
        return True    
    def replay(self, Score):
        run = True
        if Score > s:
            File = open("Score.txt", 'w')
            File.write(str(Score))
        while run:
            screen.fill((0, 0, 0))
            Asteriod().Score(Score)
            message("You Lost! Press P-Play Again or Q-Quit", RED, (180, 380), 25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return main()
                    elif event.key == pygame.K_q:
                        run = False
                        return False
            pygame.display.update()
def metor_draw(x, y):
    asteriod = pygame.image.load("practice/week10/materials/Meteorit.png")
    asteriod = pygame.transform.scale(asteriod, (50, 50))
    screen.blit(asteriod, (x, y))
def draw_Hp(a):
    a.y += 50
    hp = pygame.image.load("practice/week10/materials/HP.png")
    hp = pygame.transform.scale(hp, (50, 50))
    screen.blit(hp, (a.x*50, a.y))
    if a.y > HEIGHT-50:
        return False, 0, 0
    return True, a.x*50, a.y
    
def message(msg, color, cord, size):
    mesg = pygame.font.SysFont("bahnschrift", size).render(msg, True, color)
    screen.blit(mesg, cord)

def Pressed():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]: dx, dy, angle  = 1, 1, -135 
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:dx, dy, angle  = -1, 1, 135
    elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]: dx, dy, angle  = -1, -1, 45
    elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]: dx, dy, angle = 1, -1, -45
    elif pressed[pygame.K_DOWN]: dx, dy, angle  = 0, 1, 180
    elif pressed[pygame.K_UP]: dx, dy, angle = 0, -1, 0
    elif pressed[pygame.K_LEFT]: dx, dy, angle  = -1,  0, 90
    elif pressed[pygame.K_RIGHT]:dx, dy, angle = 1,  0, -90
    else: dx, dy, angle  = 0, 0, 0
    return dx, dy, angle

def fire_plane(x, y):
    fire = pygame.image.load('practice/week10/materials/fire_.png')
    fire = pygame.transform.scale(fire, (50, 50))
    screen.blit(fire, (x, y))
                
def draw_line():
    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(
            screen,
            WHITE,
            start_pos=(x, 0),
            end_pos=(x, WIDTH)
        )
    for y in range(0, HEIGHT, BLOCK):
        pygame.draw.line(
            screen,
            WHITE,
            start_pos=(0, y),
            end_pos=(HEIGHT, y)
        )
def random_hp():
    x, y = random.randint(0, WIDTH//50 - 1), 0
    return Point(x, y)
    
def main():
    runing = menu(True)
    x, y = WIDTH//2 - 1, HEIGHT//2
    score, PFS = 0, 0
    dx, dy, angle = 0, 0, 0
    ast = Asteriod()
    hp, Run = 4, False
    Score = 0
    while runing:
        screen.blit(fon, (0, 0))
        ast.draw()
        # draw_line()
        ast.HP(hp)
        dx, dy, angle = Pressed() 
        Plane_ = rotate_plane(angle)
        x, y = x + dx*50, y + dy*50
        if x > WIDTH-50: x = WIDTH-50
        elif x < 0: x = 0
        if y > HEIGHT-50: y = HEIGHT-50
        elif y < 0: y = 0
        if Score//10 == Score/10 or Run:
            if Run == False: a = random_hp()
            Run, x_h, y_h = draw_Hp(a)
            if x_h == x and y_h == y: 
                hp += 1
                if hp >= 4: hp = 4
                Run = False
        if score > PFS:
            ast.Points()
            score = 0
        else: score, PFS = score + (Score//10) + 2, (Score//10) + 10
        screen.blit(Plane_, (x, y))
        run = ast.game_over(x, y)
        if run == False:
            fire_plane(x, y)
            hp -= 1
            if hp == 0:
              runing = ast.replay(Score)
        Score = ast.Score(Score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
        pygame.display.update()
        clock.tick(80)

if __name__ == '__main__':
    main() 