from operator import pos

import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Titulo de la ventana")
colorFondo = (100,150,70)

#Definiendo colores de las figuras
colorCuadroUno = (255,255,255)
colorCuadroDos = (0,0,0)

#Variables
#velocidad = 15
direccion = True
posicionXCuadroUno,posicionYCuadroUno = randint(1, 400),randint(1, 300)
posicionXCuadroDos, posicionYCuadroDos = randint(1, 400),randint(1, 300)
lado = 40

while True:
    ventana.fill(color=colorFondo)
    cuadroUno = pygame.draw.rect(ventana,colorCuadroUno,(posicionXCuadroUno,posicionYCuadroUno,40,40))
    cuadroDos = pygame.draw.rect(ventana,colorCuadroDos,(posicionXCuadroDos,posicionYCuadroDos,40,40))


    #Detectar movimientos con el raton
    posicionXCuadroUno,posicionYCuadroUno = pygame.mouse.get_pos()
    posicionXCuadroUno = posicionXCuadroUno - (lado/2)
    posicionYCuadroUno = posicionYCuadroUno - (lado/2)

    #Detectar colisiones
    if cuadroUno.colliderect(cuadroDos):
        print(f"colision en {posicionXCuadroUno} : {posicionYCuadroUno}")
        posicionXCuadroDos, posicionYCuadroDos = randint(1, 360),randint(1, 260)
        cuadroDos.left = posicionXCuadroDos - (lado/2)
        cuadroDos.top = posicionYCuadroDos - (lado/2)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()