import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((1124,624))
pygame.display.set_caption("Titulo de la ventana")
colorFondo = (100,150,70)
colorRectangulo = (255,60,60)
#Cargar imagen
imagen = pygame.image.load("images/Logo_Kof.png")
#Posicion
posX1,posY1 = (10,40)

while True:
    ventana.fill(color=colorFondo)
    ventana.blit(imagen,(posX1,posY1))
    #Posiciones aleatorias
    for i in range(20):
        posX2, posY2 = randint(1,1024), randint(1,524)
        r,g,b = randint(0,255),randint(0,255),randint(0,255)
        colorRectangulo = (r,g,b)
        pygame.draw.rect(ventana,colorRectangulo,(posX2,posY2,50,80))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()