import pygame
from pygame.locals import *

from config import *
from entities import *

class P1Game:
    def __init__(self, walls = (), maxscore = 20, surface = pygame.display.set_mode(DISPLAY_MODE)):
        self.walls = walls
        self.maxscore = maxscore
        self.surface = surface
        self.surface.fill((0,0,0))

        pygame.mixer.init()
        self.musica_fondo()

        self.snake = Snake(self.surface)
        self.snake.dibujar_snake()
        self.manzana = Manzana(self.surface, self.walls)
        self.manzana.dibujar_manzana()
        self.bloque = bloques(self.surface, self.walls)
        self.bloque.dibujar_pared()

    def musica_fondo(self):
        pygame.mixer.music.load(BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1, 0)

    def musica_juego(self, sonidos):
        if sonidos == "crash":
            sonido = pygame.mixer.Sound(CRASH_SF)
        elif sonidos == 'ding':
            sonido = pygame.mixer.Sound(DING_SF)
        pygame.mixer.Sound.play(sonido)

    def reset(self):
        self.snake = Snake(self.surface)
        self.manzana = Manzana(self.surface, self.walls)
        self.bloque = bloques(self.surface, self.walls)


    def colision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def fondo_juego(self):
        bg = pygame.image.load(BACKGROUND_IMAGE)
        bg = pygame.transform.smoothscale(bg, DISPLAY_MODE)
        self.surface.blit(bg, (0,0))

    def jugar(self):
        self.fondo_juego()
        self.snake.mover_snake()
        self.manzana.dibujar_manzana()
        self.bloque.dibujar_pared()
        self.score()
        pygame.display.flip()

        # Comer Manzana
        for i in range(self.snake.largo):
            if self.colision(self.snake.x[i], self.snake.y[i], self.manzana.x, self.manzana.y):
                self.musica_juego("ding")
                self.snake.incrementar_largo()
                self.manzana.mover_manzana()

        # Se toca
        for i in range(3, self.snake.largo):
            if self.colision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.musica_juego('crash')
                raise "Se toca"

        # Toca pared
        if not (0 <= self.snake.x[0] <= DISPLAY_MODE[0] - 20 and 0 <= self.snake.y[0] <= DISPLAY_MODE[1] - 20):
            self.musica_juego('crash')
            raise "Toco Pared"

        for x in self.walls:
            for i in range(self.snake.largo):
                if self.colision(self.snake.x[i], self.snake.y[i], x[0], x[1]):
                    self.musica_juego('crash')
                    raise "Toco Pared"


    def score(self):
        font = pygame.font.SysFont('pixelar',30)
        score = font.render(f"Score: {self.snake.largo}",True,(0,0,0))
        self.surface.blit(score,(550,10))

    def perder(self):
        self.fondo_juego()
        font = pygame.font.SysFont('pixelar', 30)
        line1 = font.render(f"Game over! Tu score es {self.snake.largo}", True, (0, 0, 0))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("Para jugar otra vez presiona Enter. Para salir presiona ESC!", True, (0, 0, 0))
        self.surface.blit(line2, (200, 350))
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
                        if event.key == K_LEFT:
                            self.snake.mover_derecha()

                        if event.key == K_RIGHT:
                            self.snake.mover_izquierda()

                        if event.key == K_UP:
                            self.snake.mover_arriba()

                        if event.key == K_DOWN:
                            self.snake.mover_abajo()
            
                elif event.type == QUIT:
                    running = False
            try:

                if not pausa:
                    self.jugar()
                    if self.snake.largo == self.maxscore:
                        return True, self.snake.largo

            except Exception as e:
                self.perder()
                pausa = True
                self.reset()
            time.sleep(.1)
        return False, self.snake.largo

class P2Game:
    def __init__(self, snakepos = ((0,0),(0,0)), walls = (), maxscore = 20, surface = pygame.display.set_mode(DISPLAY_MODE)):
        self.walls = walls
        self.maxscore = maxscore
        self.surface = surface
        self.surface.fill((0,0,0))
        self.snakepos = snakepos
        self.loser = ''

        pygame.mixer.init()
        self.musica_fondo()

        self.snake = Snake(self.surface, self.snakepos[0], "Recursos/morado.jpg" )
        self.snake2 = Snake(self.surface, self.snakepos[1], "Recursos/verde.png")
        self.snake.dibujar_snake()
        self.snake2.dibujar_snake()
        self.manzana = Manzana(self.surface, self.walls)
        self.manzana.dibujar_manzana()
        self.bloque = bloques(self.surface, self.walls)
        self.bloque.dibujar_pared()

    def musica_fondo(self):
        pygame.mixer.music.load(BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1, 0)

    def musica_juego(self, sonidos):
        if sonidos == "crash":
            sonido = pygame.mixer.Sound(CRASH_SF)
        if sonidos == 'ding':
            sonido = pygame.mixer.Sound(DING_SF)
        pygame.mixer.Sound.play(sonido)

    def reset(self):
        self.snake = Snake(self.surface, self.snakepos[0], "Recursos/morado.jpg")
        self.snake2 = Snake(self.surface, self.snakepos[1], "Recursos/verde.png")
        self.manzana = Manzana(self.surface, self.walls)
        self.bloque = bloques(self.surface, self.walls)


    def colision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def fondo_juego(self):
        bg = pygame.image.load("Recursos/fondo2.jpg")
        bg = pygame.transform.smoothscale(bg, DISPLAY_MODE)
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

        for i in range(3, self.snake.largo):
            if self.colision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.musica_juego('crash')
                self.loser = '1'
                raise "Se toca 1"

        for i in range(3, self.snake2.largo):
            if self.colision(self.snake2.x[0], self.snake2.y[0], self.snake2.x[i], self.snake2.y[i]):
                self.musica_juego('crash')
                self.loser = '2'
                raise "Se toca 2"

        # Toca pared
        if not (0 <= self.snake.x[0] <= DISPLAY_MODE[0] - 20 and 0 <= self.snake.y[0] <= DISPLAY_MODE[1] - 20):
            self.musica_juego('crash')
            self.loser = '1'
            raise "Toco Pared 1"

        for x in self.walls:
            for i in range(self.snake.largo):
                if self.colision(self.snake.x[i], self.snake.y[i], x[0], x[1]):
                    self.musica_juego('crash')
                    self.loser = '1'
                    raise "Toco Pared 1"

        if not (0 <= self.snake2.x[0] <= DISPLAY_MODE[0] - 20 and 0 <= self.snake2.y[0] <= DISPLAY_MODE[1] - 20):
            self.musica_juego('crash')
            self.loser = '2'
            raise "Toco Pared 2"

        for x in self.walls:
            for i in range(self.snake2.largo):
                if self.colision(self.snake2.x[i], self.snake2.y[i], x[0], x[1]):
                    self.musica_juego('crash')
                    self.loser = '2'
                    raise "Toco Pared 2"

    def score(self):
        font = pygame.font.SysFont('pixelar',30)
        score = font.render(f"Morado: {self.snake.largo}",True,(255,255,255))
        self.surface.blit(score,(125,10))

    def score2(self):
        font = pygame.font.SysFont('pixelar',30)
        score2 = font.render(f"Verde: {self.snake2.largo}",True,(255,255,255))
        self.surface.blit(score2,(800,10))

    def perder(self):
        self.fondo_juego()
        font = pygame.font.SysFont('pixelar', 30)
        if (self.snake.largo > self.snake2.largo and self.loser != '1') or self.loser == '2':
            line0 = font.render(f"¡Snake Morado ganó este nivel!", True, (255, 0, 0))
            self.surface.blit(line0, (200, 275))
        elif (self.snake.largo < self.snake2.largo and self.loser != '2') or self.loser == '1':
            line0 = font.render(f"¡Snake Verde ganó este nivel!", True, (255, 0, 0))
            self.surface.blit(line0, (200, 275))
        line3 = font.render("Para jugar siguiente nivel presiona Enter. Para salir presiona ESC!", True, (255, 255, 255))
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
                        return False

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
                        
                    if pausa:
                        if event.key == K_RETURN:
                            running = False
                            return True

                if event.type == QUIT:
                    running = False
                    return False
            try:

                if not pausa:
                    self.jugar()
                    if self.snake.largo == self.maxscore or self.snake2.largo == self.maxscore:
                        self.perder()
                        pausa = True
                


            except Exception as e:
                self.perder()
                pausa = True

            time.sleep(.1)
        return True