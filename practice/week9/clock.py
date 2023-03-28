import pygame

pygame.init()
HEIGHT, WIDHT = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDHT))
pygame.display.set_caption("Clock")

runing = True
while runing:
    screen.fill((0, 0, 175))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    pygame.draw.line(
        screen, 
        color=(255, 255, 255), 
        start_pos=(0, 0), 
        end_pos=(500, 500), 
        width=10
    )
    pygame.draw.line(
        screen, 
        color=(255, 255, 255), 
        start_pos=(500, 0), 
        end_pos=(0, 500), 
        width=10
    )
    pygame.draw.circle(
        screen, 
        color=(0, 0, 0), 
        center=(250, 250), 
        radius=80, 
        width=10
    )
    pygame.draw.rect(
        screen, 
        color=(177, 177, 177),
        rect=pygame.Rect(160, 160, 180, 180),
        width=10
    )
    pygame.draw.polygon(
        screen,
        color=(100, 0, 0),
        points= [(160, 160), (340, 160), (250, 80)],
        width=10
    )
    pygame.display.flip()
