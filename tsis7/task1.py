import pygame, datetime
pygame.init()
clock = pygame.time.Clock()

def Angle(sec1, min1):
    if sec1 >= 0 and sec1 < 10: 
        angle_ = -300 - sec1*6
    else: 
        angle_ = 60 - sec1*6
    if min1 >= 0 and min1 < 52: 
        angle_1 = -48 - min1*6
    else: 
        angle_1 = -(min1-52)*6
    return angle_, angle_1

def rotate_minute(angle_1):
    minute = pygame.image.load('tsis7/image/min.png')
    return pygame.transform.rotate(minute, angle_1)

def rotate_second(angle_):
    second = pygame.image.load('tsis7/image/second.png')
    return pygame.transform.rotate(second, angle_)

screen = pygame.display.set_mode((820, 820))
pygame.display.set_caption('Clock')

clock_ = pygame.image.load('tsis7/image/clock.png')
second = pygame.image.load('tsis7/image/second.png')
minute = pygame.image.load('tsis7/image/min.png')

sec_1 = datetime.datetime.now().second
min_1 = datetime.datetime.now().minute

angle_, angle_1 = Angle(sec_1, min_1)

second = rotate_second(angle_)
minute = rotate_minute(angle_1)
runing = True
while runing:
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    screen.blit(clock_, (0, 0))
    if sec != sec_1: 
        angle_ -= 6
        if angle_ == -360:
            angle_ = 0
        second = rotate_second(angle_)
        sec_1 = sec
    if min_1 != min:
        angle_1 -= 6
        if angle_1 == -360:
            angle_1 == 0
        minute = rotate_minute(angle_1)
        min_1 = min
    rotated_right_rect = second.get_rect(center = (415, 415))
    rotated_right_rect1 = minute.get_rect(center = (410, 410))
    screen.blit(minute, rotated_right_rect1)
    screen.blit(second, rotated_right_rect)
    pygame.display.update()
    clock.tick(30)