import pygame
from pygame.locals import *

from config import *
from entities import *

from classgame import *

walls = [(400,40),(400,80),(400,120),(400,160),(440,160),(480,160),(520,160),(760,360),(800,360)]

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    game = P1Game(walls, surface)
    game.run()