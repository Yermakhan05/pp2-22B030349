import pygame, os, time

pygame.init()
clock = pygame.time.Clock()
HEIGHT, WIDHT = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDHT))
pygame.display.set_caption("Music")

music_name = os.listdir('tsis7/music')
fleer_image = pygame.image.load('tsis7/image_2/music.png')
fleer_image = pygame.transform.scale(fleer_image, (500, 200))

def image_music(index):
   img = pygame.image.load('tsis7/image_2/{}.jpeg'.format(index+1))
   img = pygame.transform.scale(img, (500, 300))
   return img

pygame.mixer.music.load('tsis7/music/{}'.format(music_name[0]))
pygame.mixer.music.play()

runing = True
pause = False
music_index = 0
while runing:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         runing = False
    screen.blit(image_music(music_index), (0, 0))
    screen.blit(fleer_image, (0, 300))
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE]:
        if pause:
            pygame.mixer.music.pause()
            pause = False
        else:
            pygame.mixer.music.unpause()
            pause = True
    elif pressed[pygame.K_RIGHT]:
        music_index += 1
        if music_index >= len(music_name):
            music_index = 0
        pygame.mixer.music.load('tsis7/music/{}'.format(music_name[music_index]))
        pygame.mixer.music.play()
    elif pressed[pygame.K_LEFT]:
        music_index -= 1
        if music_index < 0:
            music_index = len(music_name)-1
        
        pygame.mixer.music.load('tsis7/music/{}'.format(music_name[music_index]))
        pygame.mixer.music.play()
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.stop()

    pygame.display.update()
    time.sleep(0.2)