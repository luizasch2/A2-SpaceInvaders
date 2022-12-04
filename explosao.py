import pygame
from pygame.locals import *


class Explosao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('./sprites/Explosion_01.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_02.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_03.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_04.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_05.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_06.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_07.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_08.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_09.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_10.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_11.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_12.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_13.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_14.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_15.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_16.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_17.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_18.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_19.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_20.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_21.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_22.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_23.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_24.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_25.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_26.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_27.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_28.png'))
        self.sprites.append(pygame.image.load('./sprites/Explosion_29.png'))
    
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.animar = False

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
    # def posicao_sprite(self, x, y):
        

    def explodir(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual += 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (100*3, 100*3))





    
    


