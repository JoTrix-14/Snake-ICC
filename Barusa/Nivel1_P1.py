import pygame
from pygame.locals import *

from config import *
from entities import *

from classgame import *

walls = []

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    game = P1Game(walls, surface)
    game.run()