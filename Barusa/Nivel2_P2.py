#Intento 3

import pygame
from pygame.locals import *
import time
import random

from entities import *
from config import *

walls = [(840, 40), (880, 40), (920, 40), (960, 40), (200, 40), (240, 40), (280, 40), (320, 40), (400, 250), (440, 250), (480, 250), (520, 250), (950, 250), (990, 250), (1030, 250), (1070, 250), (4, 450), (44, 450), (84, 
450), (124, 450), (540, 450), (580, 450), (620, 450), (660, 450)]

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Joaquin M")

        pygame.mixer.init()
        self.musica_fondo()

        self.surface = pygame.display.set_mode((1000, 520))
        self.snake = Snake(self.surface, (50, 255), "Recursos/morado.jpg" )
        self.snake2 = Snake(self.surface, (750, 255), "Recursos/verde.png")
        self.snake.dibujar_snake()
        self.snake2.dibujar_snake()
        self.manzana = Manzana(self.surface, walls)
        self.manzana.dibujar_manzana()
        self.bloque = bloques(self.surface, walls)
        self.bloque.dibujar_pared()

    def musica_fondo(self):
        pygame.mixer.music.load("Recursos/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def musica_juego(self, sonidos):
        if sonidos == 'ding':
            sonido = pygame.mixer.Sound("Recursos/ding.mp3")
        pygame.mixer.Sound.play(sonido)

    def reset(self):
        self.snake = Snake(self.surface)
        self.snake2 = Snake(self.surface)
        self.manzana = Manzana(self.surface)


    def colision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def fondo_juego(self):
        bg = pygame.image.load("Recursos/fondo2.jpg")
        self.surface.blit(bg, (0,0))

    def jugar(self):
        self.fondo_juego()
        self.snake.mover_snake()
        self.snake2.mover_snake()
        self.manzana.dibujar_manzana()
        self.bloque.dibujar_pared()
        self.score()
        self.score2()
        pygame.display.flip()

        # Comer Manzana
        for i in range(self.snake.largo):
            if self.colision(self.snake.x[i], self.snake.y[i], self.manzana.x, self.manzana.y):
                self.musica_juego("ding")
                self.snake.incrementar_largo()
                self.manzana.mover_manzana()

        for i in range(self.snake2.largo):
            if self.colision(self.snake2.x[i], self.snake2.y[i], self.manzana.x, self.manzana.y):
                self.musica_juego("ding")
                self.snake2.incrementar_largo()
                self.manzana.mover_manzana()
        # Toca pared
        if not (0 <= self.snake.x[0] <= 960 and 0 <= self.snake.y[0] <= 500):
            self.musica_juego('crash')
            raise "Toco Pared"

        if not (0 <= self.snake2.x[0] <= 960 and 0 <= self.snake2.y[0] <= 500):
            self.musica_juego('crash')
            raise "Toco Pared"

    def score(self):
        font = pygame.font.SysFont('pixel',30)
        score = font.render(f"Morado: {self.snake.largo}",True,(255,255,255))
        self.surface.blit(score,(125,10))

    def score2(self):
        font = pygame.font.SysFont('pixel',30)
        score2 = font.render(f"Verde: {self.snake2.largo}",True,(255,255,255))
        self.surface.blit(score2,(800,10))

    def perder(self):
        self.fondo_juego()
        font = pygame.font.SysFont('pixel', 30)
        if self.snake.largo > self.snake2.largo:
            line0 = font.render(f"¡Snake Morado ganó este nivel, un punto para Morado!", True, (255, 255, 255))
            self.surface.blit(line0, (200, 275))
        elif self.snake.largo < self.snake2.largo:
            line0 = font.render(f"¡Snake Verde ganó este nivel, un punto para Verde!", True, (255, 255, 255))
            self.surface.blit(line0, (200, 275))
        line3 = font.render("Para jugar otra vez presiona Enter. Para salir presiona ESC!", True, (255, 255, 255))
        self.surface.blit(line3, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def run(self):
        running = True
        pausa = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pausa = False

                    if not pausa:
                        if event.key == K_a:
                            self.snake.mover_derecha()

                        if event.key == K_d:
                            self.snake.mover_izquierda()

                        if event.key == K_w:
                            self.snake.mover_arriba()

                        if event.key == K_s:
                            self.snake.mover_abajo()

                    if not pausa:
                        if event.key == K_LEFT:
                            self.snake2.mover_derecha()

                        if event.key == K_RIGHT:
                            self.snake2.mover_izquierda()

                        if event.key == K_UP:
                            self.snake2.mover_arriba()

                        if event.key == K_DOWN:
                            self.snake2.mover_abajo()
                if event.type == QUIT:
                    running = False
            try:

                if not pausa:
                    self.jugar()


            except Exception as e:
                self.perder()
                pausa = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.run()