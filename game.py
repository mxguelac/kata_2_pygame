import pygame
import random
import math

class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Bolas')

        self.players = []
        """""
        for i in range(random.randint(1,11)):
            b = Ball(random.randint(0,800), random.randint(0,600), 30, 
                 random.randint(-10, 10), random.randint(-10, 10))
            self.players.append(b)
        """""
        self.players.append(
            Ball(150, 150, 15, 10, 10)
        )
        self.players.append(
            Ball(200,200, 20, -10, -10)
        )
        self.metronomo = pygame.time.Clock()

    def main_loop(self):
        game_over = False
        while game_over == False:
            self.metronomo.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
            
            self.screen.fill((0, 255, 0))
            
            self.players[0].ball_collision(self.players[1])

            for bola in self.players:
                bola.draw(self.screen)
                bola.update(self.screen)


            pygame.display.flip()



class Ball:
    def __init__(self, x, y, radio, dx=0, dy=0):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.dx = dx
        self.dy = dy
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)
    
    def update(self, surface):
        self.x += self.dx
        self.y += self.dy

        if self.y >= surface.get_height() - self.radio or self.y <= 0 + self.radio:
            self.dy = -self.dy
        if self.x >= surface.get_width() - self.radio or self.x <= 0 + self.radio:
            self.dx = -self.dx
    
    def ball_collision(self, otra):
        distancia = math.sqrt((otra.x - self.x) ** 2 + (otra.y - self.y) ** 2)
        if distancia <= self.radio + otra.radio:
            self.dx = -self.dx
            self.dy = -self.dy
            otra.dx = -otra.dx
            otra.dy = -otra.dy

        

if __name__ == '__main__':
    juego = Bolas()
    juego.main_loop()

