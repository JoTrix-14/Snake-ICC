import pygame
from pygame.locals import *

from config import *
from entities import *

from classgame import *

walls = [(0, 0), (40, 0), (80, 0), (160, 0), (200, 0), (0, 40), (0, 120), (0, 160), (240, 40), (240, 120), (0, 480), (40, 480), (80, 480), (120, 480), (160, 480), (200, 480), (500, 80), (460, 120), (540, 120), (420, 160), (580, 160), (380, 200), (620, 200), (600, 360), (640, 360), (680, 360), (520, 360), (520, 400)]

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    game = P1Game(walls, surface)
    game.run()