import pygame, random, sys, psycopg2

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = con.cursor()
pygame.init()
HEIGHT, WIDTH = 800, 800
BLOCK = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def table():
    cur.execute('''CREATE TABLE IF NOT EXISTS public.user_name(
                    nickname character varying(60) COLLATE pg_catalog."default",
                    level integer,
                    score integer)''')
def Replay(Score, Level):
    run = True
    pygame.mixer.Sound('practice/week11/GAME2/game_over.mp3').play()
    cur.execute(
        "SELECT * FROM user_name WHERE Nickname = %s",
        (Nickname,)
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        cur.execute(
            "INSERT INTO User_name (Nickname, Level, Score) VALUES (%s, %s, %s)", 
            (Nickname, Level, Score))
    else:
        if rows[0][1] <= Level:
            if rows[0][1] == Level and rows[0][2] < Score:
                cur.execute("UPDATE User_name SET Score = %s WHERE Nickname = %s", (Score, rows[0][0]))
            cur.execute("UPDATE User_name SET Level = %s WHERE Nickname = %s", (Level, rows[0][0]))
    con.commit()
    while run:
        screen.fill((0, 220, 200))
        Snake(Score, Level).score(str(Score))
        message("You Lost! Press P-Play Again or Q-Quit", RED, [180, 380])
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
    def __init__(self, x, y, color):
        self.loc = Point(x, y, color)
    def draw(self):
        pygame.draw.rect(
            screen,
            self.loc.color,
            pygame.Rect(
                self.loc.x * BLOCK,
                self.loc.y * BLOCK,
                BLOCK,
                BLOCK,
            )
        )
    def location_food(self, snake):
        x = random.randint(1, 6)
        if x == 5: color = 'yellow'
        elif x == 2 or x == 4: color = 'blue'
        else: color = 'green'
        run = True
        while run:
            x = random.randint(0, WIDTH // BLOCK - 1)
            y = random.randint(0, HEIGHT // BLOCK - 1)
            run = snake.food_check(x, y)
        self.loc.x, self.loc.y, self.loc.color = x, y, color

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Point_s:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Snake:
    def __init__(self, Sc, Lv):
        self.POINT = [
             Point_s(
                x=WIDTH // BLOCK // 2,
                y=HEIGHT // BLOCK // 2,
            )
        ]
        self.Sc = Sc
        self.level = Lv
        self.p = Sc%20
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

        if self.POINT[0].x > WIDTH // BLOCK: Replay(self.Sc, self.level)
        elif self.POINT[0].x < 0: Replay(self.Sc, self.level)
        if self.POINT[0].y < 0: Replay(self.Sc, self.level)
        elif self.POINT[0].y > HEIGHT // BLOCK: Replay(self.Sc, self.level)
    
    def check_collision(self, food):
        if food.loc.x == self.POINT[0].x:
            if food.loc.y == self.POINT[0].y:
                if food.loc.color == 'green': self.Sc, self.p = self.Sc + 1, self.p + 1
                elif food.loc.color == 'yellow': self.Sc, self.p = self.Sc + 3, self.p + 3
                elif food.loc.color == 'blue': self.Sc, self.p = self.Sc + 2, self.p + 2
                if self.p >= 20:
                    self.level += 1
                    self.p = 0
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
    def wall(self, Wall):
        wall_list = Wall.point
        sn = self.POINT[0]
        for pt in wall_list:
            if sn.x == pt.x and sn.y == pt.y:
                Replay(self.Sc, self.level)
    def score(self, score):
        Score = pygame.font.SysFont("arial", 35).render(score,True, RED)
        screen.blit(Score, (10, 10))
        return self.Sc, self.level

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
def message(msg, color, cordi):
    mesg = pygame.font.SysFont("bahnschrift", 25).render(msg, True, color)
    screen.blit(mesg, cordi)

def welcome():
    global Nickname
    Font =  pygame.font.SysFont('Arial', 24)
    Nick = ""
    cursor = "|"
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Nick = Nick[:-1]
                elif event.key == pygame.K_RETURN:
                    runing = False
                else:
                    if len(Nick) < 14:
                        Nick += event.unicode
        Nickname = Nick
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (WIDTH//2 - 100, HEIGHT//2-20, 200, 40), width=2)
        txt = Font.render(Nickname+cursor, True, BLACK)
        screen.blit(txt, (WIDTH / 2 - 95, HEIGHT / 2 - 20))
        pygame.display.flip()

class wall:
    def __init__(self):
        self.point = []
    def update(self, snake):
        run = True
        while run:
            x = random.randint(0, WIDTH // BLOCK - 1)
            y = random.randint(0, HEIGHT // BLOCK - 1)
            run = snake.food_check(x, y)
        self.point.append(Point_s(x, y))
    def draw(self):
        for pt in self.point:
            pygame.draw.rect(
            screen,     
            WHITE,
            pygame.Rect(pt.x*BLOCK, pt.y*BLOCK,BLOCK,BLOCK)
            ) 

def main():
    runing = True
    food = Food(5, 5, 'green')
    dx, dy = 0, 0
    cur.execute(
        "SELECT * FROM User_name WHERE Nickname = %s",
        (Nickname,))
    rows = cur.fetchall()
    if len(rows) == 1: Score, Level = rows[0][2], rows[0][1]
    else: Score, Level = 0, 0
    con.commit()
    snake = Snake(Score, Level)
    Wall = wall()
    for x in range(Level):
        Wall.update(snake)
    sec, lv = 0, Level
    Event = pygame.USEREVENT
    pygame.time.set_timer(Event, 1000)
    while runing:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == Event:
                sec += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and (dx != -1 or dy != 0):
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and (dx != 1 or dy != 0):
                    dx, dy = -1, 0
                elif event.key == pygame.K_UP and (dx != 0 or dy != 1):
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and (dx != 0 or dy != -1):
                    dx, dy = 0, 1
        snake.move(dx, dy)
        if snake.game_over(): runing = Replay(Score, Level)
        if sec == 5:
            food.location_food(snake)
            sec = 0
        if snake.check_collision(food):
            if food.loc.color == 'yellow': snake.POINT.append(Point_s(snake.POINT[-1].x, snake.POINT[-1].y))
            snake.POINT.append(Point_s(snake.POINT[-1].x, snake.POINT[-1].y))
            food.location_food(snake)
            pygame.mixer.Sound('practice/week11/GAME2/check.wav').play()
            sec = 0
        snake.wall(Wall)
        if Level != lv:
            Wall.update(snake)
            lv = Level
        snake.draw()
        food.draw()
        Wall.draw()
        Score, Level = snake.score('Level: '+str(Level)+"   Score: "+str(Score)+'   Second: '+str(5-sec))
        pygame.display.update()
        clock.tick(10+(Level/10)%5)
# table()
welcome()
if __name__ == '__main__':
    main()
pygame.quit()