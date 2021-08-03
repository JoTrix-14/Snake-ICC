import pygame
from pygame.locals import *
import time
import random

from config import *

class Manzana:
    def __init__(self, Dibujo, walls, imagen = APPLE_IMG):
        self.Dibujo = Dibujo
        self.manzana = pygame.image.load(imagen).convert()
        self.manzana = pygame.transform.smoothscale(self.manzana, (SIZE,SIZE))
        self.x = 120
        self.y = 120

        self.walls = walls

    def dibujar_manzana(self):
        self.Dibujo.blit(self.manzana, (self.x, self.y))
        pygame.display.flip()

    def mover_manzana(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,11)*SIZE
        while (self.x, self.y) in self.walls:
            self.x = random.randint(1,24)*SIZE
            self.y = random.randint(1,11)*SIZE


class Snake:
    def __init__(self, Dibujo, pos = (10*SIZE,10*SIZE), imagen = SNAKE_IMG):
        self.Dibujo = Dibujo
        self.snake = pygame.image.load(imagen).convert()
        self.snake = pygame.transform.smoothscale(self.snake, (SIZE,SIZE))
        self.direccion = ''

        self.largo = 1
        self.x = [pos[0]]
        self.y = [pos[1]]

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

class bloques:
    def __init__(self, Dibujo , walls, imagen = BLOQUE_IMG):
        self.walls = walls
        self.Dibujo = Dibujo
        self.bloque = pygame.image.load(imagen).convert()

    def dibujar_pared(self):
        for x in self.walls:
            self.Dibujo.blit(self.bloque, (x[0], x[1]))
        
        pygame.display.flip()