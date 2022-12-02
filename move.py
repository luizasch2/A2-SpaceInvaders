import pygame
from settings import *
from player_config import PlayerConfig

class Move():
    def __init__(self, mode: str = 'MENU'):
        self.mode = mode
        
    def change_mode(self, new_mode: str):
        ## MENU, OPT, RES, CSS, NAVE, MONSTER, BALA, GAMEOVER, GAME
        self.mode = new_mode