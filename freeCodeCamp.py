import pygame

# Initalize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Caption and Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('images_for_game\space-ship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('rocket.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

# Game Loop
running = True
while running:
    # RGB, bakground color
    screen.fill((100,155,100))

    #playerX += 0.2
    #print(playerX)

    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right r left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + (-0.1) > 5 = 5 - 0.1
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
