# Snake version 5.0

import pygame
from pygame.locals import *

import highscore_handler
from config import *
from levels import *

import login
import menu
from classgame import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(GAMENAME)
    surface = pygame.display.set_mode(DISPLAY_MODE)
    name = login.register(surface)
    if name == None:
        exit()
    plys = menu.menu(surface)
    game_name = name
    if plys == 2:
        name1 = login.register(surface, text = "Type Name of P2")
        game_name = f'{name} v {name1}'
        if name1 == None:
            exit()
    with open(PASTGAMESFILE, 'a+') as file:
        file.write(f'{game_name}\n')
    if plys == 1:
        points = (10,15,20,30)
        curscore = 0
        for x in range(len(P1)):
            game = P1Game(walls = P1[x], maxscore = points[x],surface = surface)
            notlost, score = game.run()
            curscore += score
            if not notlost:
                break
        highscore_handler.add(game_name, curscore)
    if plys == 2:
        points = (5,10,15,20)
        snakepos = (((40, 120), (600, 120)),
                    ((40, 240), (720, 240)),
                    ((120, 200), (720, 200)),
                    ((40, 80), (840, 80)))
        for x in range(len(P2)):
            game = P2Game(walls = P2[x], snakepos = snakepos[x] ,maxscore = points[x],surface = surface)
            notended = game.run()
            if not notended:
                break
