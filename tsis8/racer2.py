import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count = 3
cnt = 0


def terminate() :
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey() :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :  # escape quits
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies) :
    x = playerRect[0]
    y = playerRect[1]
    for b in baddies :
        if abs(b['rect'][0] - x) < 20 and  abs(b['rect'][1] - y) < 20:
            return True
    return False

def playerHasHitCoin(playerRect, coins):
    for c in coins:
        if playerRect.colliderect(c['rect']):
            coins.remove(c)
            return True
    return False

def drawText(text, font, surface, x, y) :
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(False)

# fonts
font = pygame.font.SysFont(None, 30)

# sounds
gameOverSound = pygame.mixer.Sound('tsis8/music/crash.wav')
pygame.mixer.music.load('tsis8/music/car.wav')
laugh = pygame.mixer.Sound('tsis8/music/laugh.wav')

# images
playerImage = pygame.transform.scale(pygame.image.load('tsis8/images/BLUE_car.png'), (50, 50))
car3 = pygame.transform.scale(pygame.image.load('tsis8/images/RED_car.png'), (50, 50))
car4 = pygame.transform.scale(pygame.image.load('tsis8/images/RED_car.png'), (50, 50))
coin = pygame.image.load('tsis8/images/coin.jpg')
playerRect = playerImage.get_rect()
baddieImage = pygame.transform.scale(pygame.image.load('tsis8/images/RED_car.png'), (50, 50))
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load('tsis8/images/left.png')
wallRight = pygame.image.load('tsis8/images/right.png')

# "Start" screen
drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
zero = 0
if not os.path.exists("data/save.dat") :
    f = open("data/save.dat", 'w')
    f.write(str(zero))
    f.close()
v = open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()
while (count > 0) :
    # start of the game
    baddies = []
    coins = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True :  # the game loop
        score += 1  # increase score

        for event in pygame.event.get() :

            if event.type == QUIT :
                terminate()

            if event.type == KEYDOWN :
                if event.key == ord('z') :
                    reverseCheat = True
                if event.key == ord('x') :
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a') :
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w') :
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s') :
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP :
                if event.key == ord('z') :
                    reverseCheat = False
                    score = 0
                if event.key == ord('x') :
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE :
                    terminate()

                if event.key == K_LEFT or event.key == ord('a') :
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveRight = False
                if event.key == K_UP or event.key == ord('w') :
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s') :
                    moveDown = False

        # Add new baddies at the top of the screen
        if not reverseCheat and not slowCheat :
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE :
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect' : pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(random.choice(sample), (50, 50)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect' : pygame.Rect(0, 0, 126, 600),
                        'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface' : pygame.transform.scale(wallLeft, (126, 599)),
                        }
            baddies.append(sideLeft)
            sideRight = {'rect' : pygame.Rect(497, 0, 303, 600),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(wallRight, (303, 599)),
                         }
            baddies.append(sideRight)

            newCoin = {'rect': pygame.Rect(newBaddie['rect'][0] + (random.randint(140, 485)), 0 - baddieSize, 23, 47),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(coin, (23, 47)),
                      }
            coins.append(newCoin)

        # Move the player around.
        if moveLeft and playerRect.left > 0 :
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH :
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0 :
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT :
            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in baddies :
            if not reverseCheat and not slowCheat :
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat :
                b['rect'].move_ip(0, -5)
            elif slowCheat :
                b['rect'].move_ip(0, 1)

        for b in baddies[:] :
            if b['rect'].top > WINDOWHEIGHT :
                baddies.remove(b)

        for b in coins :
            if not reverseCheat and not slowCheat :
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat :
                b['rect'].move_ip(0, -5)
            elif slowCheat :
                b['rect'].move_ip(0, 1)

        for b in coins[:] :
            if b['rect'].top > WINDOWHEIGHT or b['rect'][0] > 485:
                coins.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)
        drawText('Coins: %s' % (cnt), font, windowSurface, 410, 0)

        windowSurface.blit(playerImage, playerRect)

        for b in baddies :
            windowSurface.blit(b['surface'], b['rect'])

        for b in coins :
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        if playerHasHitBaddie(playerRect, baddies) :
            cnt = 0
            #Change the speed to what it used to be
            FPS = 40
            if score > topScore :
                g = open("data/save.dat", 'w')
                g.write(str(score))
                g.write(str(cnt))
                g.close()
                topScore = score
            break

        cnt2 = 0
        if playerHasHitCoin(playerRect, coins):
            #weight of coin
            ans = random.randint(1, 10)
            cnt += ans
            cnt2 += ans
            #increase the speed of car
            if(cnt2 > 5):
                FPS += 15
                cnt2 = 0


        mainClock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    count = count - 1
    gameOverSound.play()
    time.sleep(1)
    if (count == 0) :
        laugh.play()
        drawText('Game over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
        gameOverSound.stop()