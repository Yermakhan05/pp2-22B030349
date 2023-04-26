import pygame
import time
import random
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

snake_speed = 15

# размер окна
window_x = 720
window_y = 480

# определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# инициализация
pygame.init()

# Инициализирование игрового окно
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))

# Контроллер FPS (кадры в секунду)
fps = pygame.time.Clock()

# определение положения змеи по умолчанию
snake_position = [100, 50]

# определение первых 4 блоков тела змеи
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# установка направления змеи по умолчанию к
# право
direction = 'RIGHT'
change_to = direction

# начальная оценка
score = 0
score2 = 0
up = 0
lvl = 1
name = ""

# отображение функции Score
def show_score(choice, color, font, size) :
    # создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)

    # создать объект поверхности отображения
    # score_surface
    score_surface = score_font.render('Level : ' + str(lvl) + '     ' + 'Score : ' + str(score), True, color)

    # создаем прямоугольный объект для текста
    # поверхностный объект
    score_rect = score_surface.get_rect()

    # отображение текста
    game_window.blit(score_surface, score_rect)

def welcome():
    user_name = "Write user name:"
    global name
    FONT_SIZE = 24
    FONT = pygame.font.SysFont("Arial", FONT_SIZE)
    text_box = pygame.Rect(window_x / 2 - 100, window_y / 4 + 50, 200, 40)
    text = ""
    cursor = "|"
    ch = True
    while ch:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    ch = False
                else:
                    text += event.unicode

        name = text
        # Draw the screen
        game_window.fill(white)
        pygame.draw.rect(game_window, black, text_box, 2)

        # Draw the text
        text_surface = FONT.render(text + cursor, True, black)
        game_window.blit(text_surface, (text_box.x + 5, text_box.y + 5))

        # Update the display
        pygame.display.flip()

# функция завершения игры
def game_over() :
    cur.execute(
        "INSERT INTO user_name (username) VALUES (%s)",
        (name,)
    )
    cur.execute("SELECT id FROM user_name WHERE username = %s", (name,))
    user_id = cur.fetchone()[0]
    cur.execute(
        'INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)',
        (user_id, score, lvl)
    )
    conn.commit()
    cur.close()
    conn.close()
    # создание объекта шрифта my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # создание текстовой поверхности, на которой текст
    # будет нарисовано
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # создать прямоугольный объект для текста
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # установка положения текста
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit нарисует текст на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # через 2 секунды мы выйдем из программы
    time.sleep(2)

    # деактивация библиотеки pygame
    pygame.quit()

    # quit the program
    quit()

welcome()

# Main Function
ch = True
while ch:

    # обработка ключевых событий
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            cur.execute(
                "INSERT INTO user_name (username) VALUES (%s)",
                (name, )
            )
            cur.execute("SELECT id FROM user_name WHERE username = %s", (name,))
            user_id = cur.fetchone()[0]
            cur.execute('INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET score = %s, level = %s', (user_id, score, lvl, score, lvl))
            conn.commit()
            cur.close()
            conn.close()
            ch = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'

    # Если две клавиши нажаты одновременно
    # мы не хотим, чтобы змея разделялась на две
    # направлений одновременно
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'

    # Перемещение змеи
    if direction == 'UP' :
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10

    # Механизм роста тела змеи
    # если фрукты и змеи сталкиваются, то очки
    # будет увеличено на 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] :
        score += 10
        score2 += 10
        snake_speed += 0.5
        if score2 > 30:
            score2 = 0
            up += 50
            lvl += 1
        fruit_spawn = False
    else :
        snake_body.pop()

    if not fruit_spawn :
        pos = up
        if score2 + 10 > 30:
            pos += 50
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, ((window_y - pos) // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body :
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    for i in range(0, up + 1, 50):
        pygame.draw.rect(game_window, white, (0, 480 - i, 720, 50))


    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 :
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10 - up :
        game_over()


    # Touching the snake body
    for block in snake_body[1 :] :
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over()

    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)