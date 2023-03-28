import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("BALL")
dx = 0
dy = 0
x = 250
y = 250
runing = True

while runing:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]:
        dx = 1
        dy = 1 
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        dx = -1
        dy = 1
    elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
        dx = -1
        dy = -1
    elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
        dx = 1
        dy = -1
    elif pressed[pygame.K_DOWN]:
        dx = 0
        dy = 1
    elif pressed[pygame.K_UP]:
        dx = 0
        dy = -1
    elif pressed[pygame.K_LEFT]:
        dx = -1
        dy = 0
    elif pressed[pygame.K_RIGHT]:
        dx = 1
        dy = 0
    else:
        dx = 0
        dy = 0
    x = x + dx*20
    if x > 475: x = 475
    elif x < 25: x = 25
    y = y + dy*20
    if y > 475: y = 475
    elif y < 25: y = 25
    pygame.draw.circle(
        screen, 
        color=(255, 0, 0),
        center=(x, y),
        radius=25
    )
    pygame.display.flip()
    pygame.time.Clock().tick(20)