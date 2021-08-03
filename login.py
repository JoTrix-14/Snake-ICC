import pygame
from pygame.locals import *
import time
from random import randint
import json

def register(surface, text = "Type Name of P1"):
    surface.fill((0,0,0))
    name = ''
    font = pygame.font.SysFont('arial',30)
    line1 = font.render(text, True, (250, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return None
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return name if name != '' else 'Anon' + str(randint(1,1010101010))
                if event.key == K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        name_obj = font.render(name, True, (255, 255, 255))
        surface.fill((0,0,0))
        surface.blit(name_obj , (0, 250))
        surface.blit(line1 , (400, 25))
        pygame.display.update()
    

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode((1000, 500))
    print(register(surface))