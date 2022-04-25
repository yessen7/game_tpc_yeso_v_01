import pygame
import math

pygame.init()
running = True
screen = pygame.display.set_mode((800, 600))

class player:
    number_of_player = 0

    def __init__(self, img, playerX, playerY, p_changeX, p_changeY):
        self.playerIMG = pygame.image.load('{}'.format(img))
        self.playerX = playerX
        self.playerY = playerY
        self.p_changeX = p_changeX
        self.p_changeY = p_changeY
        self.img = img

    def fulinfo(self):
        return '{} {} {}'.format(self.img, self.playerX,self.playerY)

#rocket1
rocket = player('rocket.png', 470, 250, 0, 0)
#ufo1
ufo = player('ufo.png', 270, 250, 0, 0)

def load(name):
    screen.blit(name.playerIMG, (name.playerX, name.playerY))

def isCollision(p1, p2):
    d = math.sqrt((math.pow(p1.playerX - p2.playerX, 2)) + (math.pow(p1.playerY - p2.playerY, 2)))
    if d < 64:
        return True
    else:
        return False

while running:
    screen.fill((100, 100, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #rocket movement keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.p_changeX = -0.4
            if event.key == pygame.K_RIGHT:
                rocket.p_changeX = 0.4
            if event.key == pygame.K_UP:
                rocket.p_changeY = -0.4
            if event.key == pygame.K_DOWN:
                rocket.p_changeY = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                rocket.p_changeX = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                rocket.p_changeY = 0

        #ufo movement keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ufo.p_changeX = -0.4
            if event.key == pygame.K_d:
                ufo.p_changeX = 0.4
            if event.key == pygame.K_w:
                ufo.p_changeY = -0.4
            if event.key == pygame.K_s:
                ufo.p_changeY = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                ufo.p_changeX = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                ufo.p_changeY = 0

    #boarders of rocket
    if rocket.playerX <= 0:
        rocket.playerX = 0
    elif rocket.playerX >= 736:
       rocket.playerX = 736
    if rocket.playerY <= 0:
        rocket.playerY = 0
    elif rocket.playerY >= 536:
        rocket.playerY = 536

    #boarders of ufo
    if ufo.playerX <= 0:
        ufo.playerX = 0
    elif ufo.playerX >= 736:
        ufo.playerX = 736
    if ufo.playerY <= 0:
        ufo.playerY = 0
    elif ufo.playerY >= 536:
        ufo.playerY = 536

    d = math.sqrt(((ufo.playerX - rocket.playerX) ** 2) + ((ufo.playerY - rocket.playerY) ** 2))
    if d <= 64:
        rocket.playerX += 10
        rocket.playerY -= 10
        ufo.playerX -= 10
        ufo.playerY += 10

    # Collision
    collision = isCollision(rocket, ufo)
    if collision:
        rocket.playerX += 10
        rocket.playerY -= 10
        ufo.playerX -= 10
        ufo.playerY += 10


    rocket.playerX += rocket.p_changeX
    rocket.playerY += rocket.p_changeY
    ufo.playerX += ufo.p_changeX
    ufo.playerY += ufo.p_changeY

    # Functions for running
    load(rocket)
    load(ufo)
    pygame.display.update()
