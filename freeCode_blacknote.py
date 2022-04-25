import pygame

#playerIMG = pygame.image.load('"{}"'.format(img))

#img = 'rocket.png'
#playerIMG = ('{}'.format(img))
#print(playerIMG)

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

rocket = player('rocket.png', 270, 250, 0, 0)
print(rocket.fulinfo())
ufo = player('ufo.png', 470, 250, 0, 0)
def load(name):
    screen.blit(name.playerIMG, (name.playerX, name.playerY))
print(rocket.playerIMG)

pygame.init()
running = True
screen = pygame.display.set_mode((800, 600))

def movement(object, velocity, z, x, c, v):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_:
            object.p_changeX = velocity
        if event.key == pygame.K_(x):
            object.p_changeX = velocity
        if event.key == pygame.K_(c):
            object.p_changeY = velocity
        if event.key == pygame.K_(v):
            object.p_changeY = velocity
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_(z) or pygame.K_(x):
            object.p_changeX = 0
        if event.key == pygame.K_(c) or pygame.K_(v):
            object.p_changeY = 0

while running:
    screen.fill((100, 150, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        load(rocket)
        load(ufo)
        movement(rocket, 0.4, "a", "d", "w", "s")
        pygame.display.update()
print(rocket.p_changeX)



