import pygame
pygame.init()

#Creación de la ventana del juego
pantalla = pygame.display.set_mode((800, 600))

#Titulo de la pantalla
pygame.display.set_caption('Hola mundo')
game_over = False

metronomo = pygame.time.Clock()

azul = 0

#Bucle principal
while game_over == False:
    ms = metronomo.tick(60)
    print(ms)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True

    azul += 1
    if azul > 255:
        azul = 0

    pantalla.fill((0,0, azul))
    pygame.display.flip()