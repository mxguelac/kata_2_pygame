import pygame
import random

class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Bolas')

        self.player = Ball(400, 300, 30, (255, 255, 255), random.randint(-15,15), random.randint(-10, 10))
        self.metronomo = pygame.time.Clock()

    def main_loop(self):
        game_over = False
        while game_over == False:
            self.metronomo.tick(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True
            
            self.screen.fill((0, 255, 0))
            self.player.draw(self.screen)
            self.player.update(self.screen)
            
            pygame.display.flip()



class Ball:
    def __init__(self, x, y, radio, color = (255, 255, 255), dx=0, dy=0):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
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
        

if __name__ == '__main__':
    bola = Bolas()
    bola.main_loop()

