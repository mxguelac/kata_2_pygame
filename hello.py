import pygame

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hola mundo')

game_over = False
while game_over == False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True


    pantalla.fill((0,0, 255))
    pygame.display.flip()