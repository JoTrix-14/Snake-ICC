import pygame
from pygame.locals import *

import highscore_handler
from config import *

def menu(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('pixelar', 40)
    line1 = font.render(f"JUGAR", True, (0, 0, 0))
    line2 = font.render(f"HIGHSCORES", True, (0, 0, 0))
    line3 = font.render(f"SALIR", True, (0, 0, 0))
    line4 = font.render(f"PAST GAMES", True, (0, 0, 0))

    button_1 = pygame.Rect(250,50,500,100)
    button_2 = pygame.Rect(250,160,500,100)
    button_3 = pygame.Rect(250,270,500,100)
    button_4 = pygame.Rect(10,10,200,40)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_1.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        res = plyrs(surface) 
                        if res != None:
                            return res
            if button_2.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return highscores(surface)
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        exit()
            if button_4.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return pastgames(surface)
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (61, 227, 179), button_1)
        pygame.draw.rect(surface, (61, 227, 179), button_2)
        pygame.draw.rect(surface, (61, 227, 179), button_3)
        pygame.draw.rect(surface, (61, 227, 179), button_4)

        surface.blit(line1, (400, 90))
        surface.blit(line2, (400, 190))
        surface.blit(line3, (400, 290))
        surface.blit(line4, (20, 20))
        pygame.display.update()
    
def plyrs(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('pixelar', 40)
    line1 = font.render(f"1 Player", True, (0, 0, 0))
    line2 = font.render(f"2 Player", True, (0, 0, 0))
    line3 = font.render(f"REGRESAR", True, (0, 0, 0))

    button_1 = pygame.Rect(250,50,500,100)
    button_2 = pygame.Rect(250,160,500,100)
    button_3 = pygame.Rect(250,270,500,100)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_1.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return 1
            if button_2.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return 2
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return menu(surface)
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (127, 216, 239), button_1)
        pygame.draw.rect(surface, (127, 216, 239), button_2)
        pygame.draw.rect(surface, (127, 216, 239), button_3)
        surface.blit(line1, (400, 90))
        surface.blit(line2, (400, 190))
        surface.blit(line3, (400, 290))
        pygame.display.update()

def highscores(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('pixelar', 40)
    line1 = font.render(f"Highscores", True, (249, 159, 251))
    highscores = highscore_handler.get()
    highscores = [f'{x} : {highscores[x]}'for x in highscores.keys()]
    line2 = [font.render(x, True, (255, 255, 255)) for x in highscores][:5]
    line3 = font.render(f"REGRESAR", True, (0,0,0))

    button_3 = pygame.Rect(250,270,500,100)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return menu(surface)
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (249, 159, 251), button_3)
        surface.blit(line1 , (400, 25))
        down = 0
        for x in line2:
            surface.blit(x, (400, 90+down))
            down += 27
        surface.blit(line3, (400, 290))
        pygame.display.update()

def pastgames(surface):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('pixelar', 40)
    line1 = font.render(f"Last 5 Games", True, (249, 159, 251))
    with open(PASTGAMESFILE, 'r') as file:
        line2 = [font.render(x.strip('\n'), True, (255, 255, 255)) for x in file][-5:]
    line3 = font.render(f"Salir", True, (0,0,0))
    #button_1 = pygame.Rect(250,50,500,100)
    #button_2 = pygame.Rect(250,160,500,100)
    button_3 = pygame.Rect(250,270,500,100)

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if button_3.collidepoint(mx, my):
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        return menu(surface)
            elif event.type == QUIT:
                exit()
        pygame.draw.rect(surface, (249, 159, 251), button_3)
        surface.blit(line1 , (400, 25))
        down = 0
        for x in line2:
            surface.blit(x, (400, 90+down))
            down += 27
        surface.blit(line3, (400, 290))
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake v5.0")
    surface = pygame.display.set_mode((1000, 500))
    print(menu(surface))

