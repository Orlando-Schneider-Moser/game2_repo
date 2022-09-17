import pygame, sys
from pygame.locals import QUIT


#==================================================
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
#==================================================




#==================================================

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_escape:
                break
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

pygame.quit()
sys.exit()

