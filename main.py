import pygame
from settings import *
from player_config import PlayerConfig
from bullet import Bullet
from move import Move
import sys

#init pygame
pygame.init()

background = scene_config()
player = PlayerConfig()
move = Move()
bullet = Bullet()

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

    if move.mode == 'OPT':
            background = support_images["opt"]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        move.mode = 'MENU'
                    if event.key == pygame.K_s:
                        move.mode = 'RES'
                    if event.key == pygame.K_c:
                        move.mode = 'CSS'

    if move.mode == 'RES':
        background = support_images["res"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if move.mode == 'CSS':
        background = support_images["css"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    if move.mode == 'GAME':
        backgrond = support_images["game"]

        # Moviment da nave
        playerX_change = 0
        player.movimento()
        player.change_position(player.X + playerX_change)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.blit(player.X, player.Y) 





    pygame.display.update()