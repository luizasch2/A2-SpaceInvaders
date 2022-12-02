import pygame
from settings import *
from player_config import PlayerConfig
from move import Move
import sys

#init pygame
pygame.init()

background = scene_config()
player = PlayerConfig()
move = Move()

while True:
    screen.blit(background, (0, 0))
    if move.mode == 'MENU':
        background = support_images["menu"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        background = support_images["game"]
                        move.mode = 'GAME'
                if event.key == pygame.K_ESCAPE:
                    move.mode = 'OPT'
                    print('OPT')
    if move.mode == 'OPT':
        background = support_images["opt"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
    


    pygame.display.update()