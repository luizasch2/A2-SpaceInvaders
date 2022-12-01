import pygame
from settings import *
from player_config import PlayerConfig

#init pygame
pygame.init()

background = scene_config()
player = PlayerConfig()

while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()