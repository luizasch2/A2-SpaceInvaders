import pygame
from pygame.locals import *


class Explosao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(1,30):
            self.sprites.append(pygame.image.load(f'./sprites/Explosion_{i}.png'))
    
        self.index = 0
        self.image = self.sprites[self.index]
        self.image = pygame.transform.scale(self.image, (100*4, 100*4))
        self.counter = 0

    def update(self):
        self.counter += 0.05
        if self.counter >= 10:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.sprites):
                self.kill()
            else:
                self.image = self.sprites[self.index]
                self.image = pygame.transform.scale(self.image, (100*4, 100*4))
    
    
    def posicao(self, x, y):      
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

