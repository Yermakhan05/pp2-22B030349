import pygame, sys

pygame.init()
clock = pygame.time.Clock()

HEIGHT, WIDTH = ()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('')

def main():
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        clock.tick(60)
if __name__ == '__main__':
    main()

pygame.quit()