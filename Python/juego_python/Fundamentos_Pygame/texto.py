from operator import pos

import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((500,400))
pygame.display.set_caption("Titulo de la ventana")
colorFondo = (100,150,70)

#Definiendo colores de las figuras
colorCuadroUno = (255,255,255)
colorCuadroDos = (0,0,0)
colorTexto = (255,255,255)

#Variables
#velocidad = 15
direccion = True
posicionXCuadroUno,posicionYCuadroUno = randint(1, 500),randint(1, 360)
posicionXCuadroDos, posicionYCuadroDos = randint(1, 500),randint(1, 360)
lado = 40
#cadena = "Texto de prueba"
tamanno = 40
tipoFuente = "Verdana"

#Preparacion de funte / texto
fuente = pygame.font.SysFont(tipoFuente,tamanno)
texto = fuente.render("",True,colorTexto)

while True:
    ventana.fill(color=colorFondo)

    #Mostrar texto
    ventana.blit(texto,(10,50))

    cuadroUno = pygame.draw.rect(ventana,colorCuadroUno,(posicionXCuadroUno,posicionYCuadroUno,40,40))
    cuadroDos = pygame.draw.rect(ventana,colorCuadroDos,(posicionXCuadroDos,posicionYCuadroDos,40,40))


    #Detectar movimientos con el raton
    posicionXCuadroUno,posicionYCuadroUno = pygame.mouse.get_pos()
    posicionXCuadroUno = posicionXCuadroUno - (lado/2)
    posicionYCuadroUno = posicionYCuadroUno - (lado/2)

    #Detectar colisiones
    if cuadroUno.colliderect(cuadroDos):
        #print(f"colision en {posicionXCuadroUno} : {posicionYCuadroUno}")
        cadena = f"colision en {posicionXCuadroUno} : {posicionYCuadroUno}"
        texto = fuente.render(cadena, True, colorTexto)

        posicionXCuadroDos, posicionYCuadroDos = randint(1, 460),randint(1, 360)
        cuadroDos.left = posicionXCuadroDos - (lado/2)
        cuadroDos.top = posicionYCuadroDos - (lado/2)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()