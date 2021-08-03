#Intento 3
import pygame
from pygame.locals import *
import time
import random

from entities import *
from config import *

class Manzana:
    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.manzana = pygame.image.load("Recursos/manzi.png").convert()
        self.x = 120
        self.y = 120

    def dibujar_manzana(self):
        self.Dibujo.blit(self.manzana, (self.x, self.y))
        pygame.display.flip()

    def mover_manzana(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,11)*SIZE

class Snake:
    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.snake = pygame.image.load("Recursos/morado.jpg").convert()
        self.direccion = ''

        self.largo = 1
        #ACA DEFINES EL SNAKE MORADO
        self.x = [140]
        self.y = [225]

    def mover_derecha(self):
        self.direccion = 'derecha'

    def mover_izquierda(self):
        self.direccion = 'izquierda'

    def mover_arriba(self):
        self.direccion = 'arriba'

    def mover_abajo(self):
        self.direccion = 'abajo'

    def mover_snake(self):
        for i in range(self.largo-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direccion == 'derecha':
            self.x[0] -= SIZE
        if self.direccion == 'izquierda':
            self.x[0] += SIZE
        if self.direccion == 'arriba':
            self.y[0] -= SIZE
        if self.direccion == 'abajo':
            self.y[0] += SIZE

        self.dibujar_snake()

    def dibujar_snake(self):
        for i in range(self.largo):
            self.Dibujo.blit(self.snake, (self.x[i], self.y[i]))

        pygame.display.flip()

    def incrementar_largo(self):
        self.largo += 1
        self.x.append(-1)
        self.y.append(-1)

class Snake2:
    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.snake2 = pygame.image.load("Recursos/verde.png").convert()
        self.direccion = ''

        self.largo = 1
        #ACA DEFINES EN DONDE COMIENZA SNAKE VERDE
        self.x = [750]
        self.y = [225]

    def mover_derecha(self):
        self.direccion = 'derecha'

    def mover_izquierda(self):
        self.direccion = 'izquierda'

    def mover_arriba(self):
        self.direccion = 'arriba'

    def mover_abajo(self):
        self.direccion = 'abajo'

    def mover_snake2(self):
        for i in range(self.largo-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direccion == 'derecha':
            self.x[0] -= SIZE
        if self.direccion == 'izquierda':
            self.x[0] += SIZE
        if self.direccion == 'arriba':
            self.y[0] -= SIZE
        if self.direccion == 'abajo':
            self.y[0] += SIZE

        self.dibujar_snake2()

    def dibujar_snake2(self):
        for i in range(self.largo):
            self.Dibujo.blit(self.snake2, (self.x[i], self.y[i]))

        pygame.display.flip()

    def incrementar_largo2(self):
        self.largo += 1
        self.x.append(-1)
        self.y.append(-1)

class bloques:

    def __init__(self, Dibujo):
        self.Dibujo = Dibujo
        self.bloque = pygame.image.load("Recursos/piedra_2.jpg").convert()

        self.x = 40
        self.y = 40

    def dibujar_pared(self):
        temp = [(self.x*8, self.y*5), (self.x*9, self.y*5), (self.x*10, self.y*5), (self.x*0, self.y*0), (self.x, self.y*0), (self.x*2, self.y*0), (self.x*8, self.y*0), (self.x*9, self.y*0), (self.x*10, self.y*0), (self.x*11, self.y*0), (self.x*12, self.y*0), (self.x*13, self.y*0), (self.x*14, self.y*0), (self.x*15, self.y*0), (self.x*16, self.y*0), (self.x*17, self.y*0), (self.x*18, self.y*0), (self.x*19, self.y*0), (self.x*20, self.y*0), (self.x*21, self.y*0), (self.x*22, self.y*0), (self.x*23, self.y*0), (self.x*24, self.y*0), (self.x*23, self.y*12), (self.x*22, self.y*12), (self.x*0, self.y), (self.x*0, self.y*2), (self.x*0, self.y*3), (self.x*0, self.y*4), (self.x*0, self.y*5), (self.x*0, self.y*6), (self.x*0, self.y*7), (self.x*0, self.y*8), (self.x*0, self.y*9), (self.x*0, self.y*10), (self.x*0, self.y*11), (self.x*0, self.y*12), (self.x*24, self.y), (self.x*24, self.y*2), (self.x*24, self.y*3), (self.x*24, self.y*4), (self.x*24, self.y*5), (self.x*24, self.y*6), (self.x*24, self.y*7), (self.x*24, self.y*8), (self.x*24, self.y*9), (self.x*24, self.y*10), (self.x*24, self.y*11), (self.x*24, self.y*12), (self.x, self.y*12), (self.x*2, self.y*12), (self.x*3, self.y*12), (self.x*4, self.y*12), (self.x*5, self.y*12), (self.x*6, self.y*12), (self.x*7, self.y*12), (self.x*8, self.y*12), (self.x*9, self.y*12), (self.x*10, self.y*12), (self.x*11, self.y*12), (self.x*12, self.y*12), (self.x*13, self.y*12), (self.x*14, self.y*12), (self.x*15, self.y*12), (self.x*16, self.y*12), (self.x*16, self.y*8), (self.x*17, self.y*8), (self.x*18, self.y*8)]
        print(temp)
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Joaquin M")

        pygame.mixer.init()
        self.musica_fondo()

        self.surface = pygame.display.set_mode((1000, 520))
        self.snake = Snake(self.surface)
        self.snake2 = Snake2(self.surface)
        self.snake.dibujar_snake()
        self.snake2.dibujar_snake2()
        self.manzana = Manzana(self.surface)
        self.manzana.dibujar_manzana()
        self.bloque = bloques(self.surface)
        self.bloque.dibujar_pared()

    def musica_fondo(self):
        pygame.mixer.music.load("Recursos/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def musica_juego(self, sonidos):
        if sonidos == 'ding':
            sonido = pygame.mixer.Sound("ding.mp3")
        pygame.mixer.Sound.play(sonido)

    def reset(self):
        self.snake = Snake(self.surface)
        self.snake2 = Snake2(self.surface)
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
        self.snake2.mover_snake2()
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
                self.snake2.incrementar_largo2()
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
