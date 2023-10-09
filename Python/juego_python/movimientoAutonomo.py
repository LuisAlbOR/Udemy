import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Titulo de la ventana")
colorFondo = (100,150,70)
colorFigura = (255,255,255)

#Variables
velocidad = 0.1
direccion = True
posX,posY = randint(1,400),randint(1,300)

while True:
    ventana.fill(color=colorFondo)
    pygame.draw.rect(ventana,colorFigura,(posX,posY,40,40))
    #Movimiento
    if direccion == True:
        if posX <(400-40):
            posX += velocidad
        else:
            direccion = False
    else:
        if posX > 1:
            posX -= velocidad
        else:
            direccion = True

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()