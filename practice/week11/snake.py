import pygame, random, sys, time

pygame.init()
HEIGHT, WIDTH = 800, 800
BLOCK = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
def Replay(Score):
    run = True
    pygame.mixer.Sound('practice/week11/GAME2/game_over.mp3').play()
    while run:
        screen.fill((0, 220, 200))
        Snake().score(Score)
        message("You Lost! Press P-Play Again or Q-Quit", RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return main()
                elif event.key == pygame.K_q:
                    sys.exit()
        pygame.display.update()

class Food:
    def __init__(self, x, y):
        self.loc = Point(x, y)
    def draw(self):
        pygame.draw.rect(
            screen,
            GREEN,
            pygame.Rect(
                self.loc.x * BLOCK,
                self.loc.y * BLOCK,
                BLOCK,
                BLOCK,
            )
        )
    def location_food(self, snake):
        run = True
        while run:
            x = random.randint(0, WIDTH // BLOCK - 1)
            y = random.randint(0, HEIGHT // BLOCK - 1)
            run = snake.food_check(x, y)
        self.loc.x, self.loc.y = x, y

class add:
    def __init__(self):
        self.loc = Point(2, 2)
    def draw(self):
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(
                self.loc.x * BLOCK,
                self.loc.y * BLOCK,
                BLOCK,
                BLOCK,
            )
        )
    def location_add(self, snake):
        run = True
        while run:
            x = random.randint(0, WIDTH // BLOCK - 1)
            y = random.randint(0, HEIGHT // BLOCK - 1)
            run = snake.food_check(x, y)
        self.loc.x, self.loc.y = x, y

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Snake:
    def __init__(self):
        self.POINT = [
             Point(
                x=WIDTH // BLOCK // 2,
                y=HEIGHT // BLOCK // 2,
            )
        ]
    def draw(self):
        cordinate = self.POINT[0]
        pygame.draw.rect(
            screen,     
            RED,
            pygame.Rect(cordinate.x*BLOCK, cordinate.y*BLOCK,BLOCK,BLOCK)
        )
        for cordinate in self.POINT[1:]:
            pygame.draw.rect(
            screen,     
            BLUE,
            pygame.Rect(cordinate.x*BLOCK, cordinate.y*BLOCK,BLOCK,BLOCK)
        )
    def move(self, dx, dy):
        for idx in range(len(self.POINT)-1,0, -1):
            cordinate = self.POINT[idx]
            cordinate.x = self.POINT[idx-1].x
            cordinate.y = self.POINT[idx-1].y
        
        point = self.POINT[0]
        point.x += dx
        point.y += dy

        if self.POINT[0].x > WIDTH // BLOCK:
            self.POINT[0].x = 0
        elif self.POINT[0].x < 0:
            self.POINT[0].x = (WIDTH // BLOCK)
        if self.POINT[0].y < 0:
            self.POINT[0].y = (WIDTH // BLOCK)
        elif self.POINT[0].y > HEIGHT // BLOCK:
            self.POINT[0].y = 0
    
    def check_collision(self, food):
        if food.loc.x == self.POINT[0].x:
            if food.loc.y == self.POINT[0].y:
                return True
        return False
    def game_over(self):
        cordinate0 = self.POINT[0]
        for cordinate in self.POINT[1:]:
            if cordinate.x == cordinate0.x:
                if cordinate.y == cordinate0.y:
                    return True
        return False
    def food_check(self, x, y):
        for cordinate in self.POINT:
            if cordinate.x == x:
                if cordinate.y == y:
                    return True
        return False
    def score(self, Score_):
        Score = pygame.font.SysFont("arial", 35).render("You Score: "+str(Score_),True, RED)
        screen.blit(Score, (10, 10))

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
def message(msg, color):
    mesg = pygame.font.SysFont("bahnschrift", 25).render(msg, True, color)
    screen.blit(mesg, [180, 380])

def main():
    runing = True
    snake = Snake()
    food = Food(5, 5)
    Add = add()
    dx, dy = 0, 0
    Score = 0
    while runing:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and (dx != -1 or dy != 0):
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and (dx != 1 or dy != 0):
                    dx, dy = -1, 0
                elif event.key == pygame.K_UP and (dx != 0 or dy != 1):
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and (dx != 0 or dy != -1):
                    dx, dy = 0, 1
        press = pygame.key.get_pressed()
        snake.move(dx, dy)
        if snake.game_over():
            runing = Replay(Score)

        if snake.check_collision(food):
            snake.POINT.append(Point(snake.POINT[-1].x, snake.POINT[-1].y))
            Score += 1
            food.location_food(snake)
            pygame.mixer.Sound('practice/week11/GAME2/check.wav').play()
        if snake.check_collision(Add):
            if len(snake.POINT) == 1:
                Replay(Score)
            snake.POINT.remove(snake.POINT[len(snake.POINT)-1])
            Add.location_add(snake)
            pygame.mixer.Sound('practice/week11/GAME2/check.wav').play()
        snake.draw()
        food.draw()
        Add.draw()
        # draw_line()
        snake.score(Score)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
pygame.quit()