import pygame
import sys

#General setup
pygame.init() #opposite of pygame.quit()
clock = pygame.time.Clock()

#Create the display surface
screen = pygame.display.set_mode((800,600))
second_surface = pygame.Surface([200,200])
second_surface.fill((0,0,150))

am = pygame.image.load('am.jpeg')
am_rect = am.get_rect()
print(am_rect.center)
am_rect = am.get_rect(topleft = [100,200])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100,150,100))
    screen.blit(second_surface,(50,50))
    screen.blit(am,am_rect)

    am_rect.left += 5

    pygame.display.flip()
    clock.tick(60)
