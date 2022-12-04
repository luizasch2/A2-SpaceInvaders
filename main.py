import pygame
from settings import *
from player_config import PlayerConfig
from bullet import Bullet
from move import Move
import sys
from enemy import Enemy
import random
from pygame import mixer

#init pygame
pygame.init()

background = scene_config()
player = PlayerConfig()
move = Move()
bullet = Bullet()
enemies = [Enemy(random.randint(65, x_pix - 65), random.randint(75, 150)) for _ in range(num_of_enemies)]


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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'OPT'
                if event.key == pygame.K_1:
                    support_images = support_images_big
                    num_of_enemies = 10
                    x_pix, y_pix = 1024, 768
                    change_res(x_pix, y_pix)
                    player.change_spawn(x_pix/2 - 30, y_pix - 120)
                    enemies = [Enemy(random.randint(65, x_pix - 65), random.randint(75, 150)) for _ in range(num_of_enemies)]
                    for enemy in enemies:
                        enemy.bullet = Bullet()
                        enemy.bullet.config_enemy_image()
                    bullet = Bullet()
                if event.key == pygame.K_ESCAPE:
                    num_of_enemies = 6
                    support_images = support_images_small
                    x_pix, y_pix = 800, 600
                    change_res(x_pix, y_pix)
                    player.change_spawn(x_pix/2 - 30, y_pix - 120)
                    enemies = [Enemy(random.randint(65, x_pix - 65), random.randint(75, 150)) for _ in range(num_of_enemies)]
                    for enemy in enemies:
                        enemy.bullet = Bullet()
                        enemy.bullet.config_enemy_image()
                    bullet = Bullet()

    if move.mode == 'CSS':
        background = support_images["css"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'MENU'
                if event.key == pygame.K_1:
                    move.mode = 'NAVE'
                if event.key == pygame.K_2:
                    move.mode = 'MONSTER'
                if event.key == pygame.K_3:
                    move.mode = 'BALA'
                if event.key == pygame.K_ESCAPE:
                    player.change_image('./img/001-nave-espacial.png')
                    for enemy in enemies:
                        enemy.change_skin('./img/002-ghost.png')
                        enemy.change_skin_hard('./img/003-ghost.png')
                    bullet.change_image('./img/001-bullet.png')

    if move.mode == 'NAVE':
        background = support_images["nave"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'CSS'
                if event.key == pygame.K_1:
                    player.change_image('./img/aircraft.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_2:
                    player.change_image('./img/rocket.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_3:
                    player.change_image('./img/ufo.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_4:
                    player.change_image('./img/tardis.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_5:
                    player.change_image('./img/K9.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_ESCAPE:
                    player.change_image('./img/001-nave-espacial.png')
                    move.mode = 'CSS'
    
    if move.mode == 'MONSTER':
        background = support_images["monster"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'CSS'
                if event.key == pygame.K_1:
                    for enemy in enemies:
                        enemy.change_skin('./img/000-ghost.png')
                        enemy.change_skin_hard('./img/001-ghost.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_2:
                    for enemy in enemies:
                        enemy.change_skin('./img/004-ghost.png')
                        enemy.change_skin_hard('./img/005-ghost.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_3:
                    for enemy in enemies:
                        enemy.change_skin('./img/ufo-1.png')
                        enemy.change_skin_hard('./img/ufo-2.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_4:
                    for enemy in enemies:
                        enemy.change_skin('./img/dalek.png')
                        enemy.change_skin_hard('./img/dalek-2.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_5:
                    for enemy in enemies:
                        enemy.change_skin('./img/cyberman.png')
                        enemy.change_skin_hard('./img/cyberman-2.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_ESCAPE:
                    for enemy in enemies:
                        enemy.change_skin('./img/002-ghost.png')
                        enemy.change_skin_hard('./img/003-ghost.png')
                    move.mode = 'CSS'
    if move.mode == 'BALA':
        background = support_images["bala"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'CSS'
                if event.key == pygame.K_1:
                    move.mode = 'CSS'
                    bullet.change_image('./img/003-bullet.png')
                if event.key == pygame.K_2:
                    move.mode = 'CSS'
                    bullet.change_image('./img/002-bullet.png')
                if event.key == pygame.K_3:
                    move.mode = 'CSS'
                    bullet.change_image('./img/004-bullet.png')
                if event.key == pygame.K_4:
                    move.mode = 'CSS'
                    bullet.change_image('./img/laser.png')
                if event.key == pygame.K_5:
                    move.mode = 'CSS'
                    bullet.change_image('./img/laser2.png')
                if event.key == pygame.K_ESCAPE:
                    move.mode = 'CSS'
                    bullet.change_image('./img/001-bullet.png')


    if move.mode == 'GAME':
        backgrond = support_images["game"]

        # Moviment da nave
        playerX_change = 0
        player.movimento()
        player.change_position(player.X + playerX_change)
        if background != support_images["gameover"]:
            if bullet.state == 'stopped':
                player.fire(bullet=bullet)

        # movimento da bala
        if bullet.Y <= 0:
            bullet.change_position(new_x = bullet.X, new_y = y_pix - 120)
            bullet.change_state('stopped')

        if bullet.state == 'fire':
            bullet.fire(bullet.X, bullet.Y)
            bullet.change_position(bullet.X, bullet.Y - 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.blit(player.X, player.Y) 

        i = 0
        for enemy in enemies:
            i += 1
            if enemy.X <= 0 or enemy.X >= x_pix - 64:
                enemy.change_vel(- enemy.vel)
            enemy.change_position(enemy.X + enemy.vel, enemy.Y)

            # colisão
            collision = move.isCollision(enemy, bullet)

            if collision:
                collision_sound = mixer.Sound('./sounds/explosion.wav')
                collision_sound.play()
                bullet.change_position(new_x = bullet.X, new_y = y_pix - 120)
                bullet.change_state('stopped')  
                enemy.change_position(random.randint(65, x_pix - 65), random.randint(50, 150))

        for enemy in enemies:
            enemy.blit(enemy.X, enemy.Y)





    pygame.display.update()