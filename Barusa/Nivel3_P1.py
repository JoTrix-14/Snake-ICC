import pygame
from pygame.locals import *

from config import *
from entities import *

from classgame import *

walls = [(200, 200), (240, 240), (280, 280), (320, 320), (400, 320), (440, 360), (480, 400), (580, 480), (620, 480), (600, 40), (640, 40), (680, 40), (720, 40), (760, 40), (760, 60), (760, 80), (760, 100)]

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode(DISPLAY_MODE)
    game = P1Game(walls, surface)
    game.run()