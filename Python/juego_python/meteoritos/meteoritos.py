import pygame as pg
import sys
from pygame.locals import *
#Importando nuestras clases
from clases import jugador

#Declaración de variables
ancho = 480
alto = 700

#Boolean para ver si se puede jugar
jugando = True

#Definiendo la función principal
def cargarFondo():
    pg.init()
    ventana = pg.display.set_mode((ancho,alto))

    #Se carga la imagen de fondo
    fondo = pg.image.load("imagenes/fondo.png")

    #Titulo
    pg.display.set_caption("Meteoritos")

    #Creando objeto jugador
    nave = jugador.Nave()

    #Ciclo de juego
    while True:

        ventana.blit(fondo, (0, 0))
        nave.visualizarJugador(ventana)


        #Verificar el disparo
        if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:

                x.visualizarDisparo(ventana)
                x.recorrido()
                if x.rect.top <- 10:
                    nave.listaDisparo.remove(x)

        nave.mover()
        for evento in pg.event.get():
            if evento.type == QUIT:
                pg.quit()
                sys.exit()
            elif evento.type == pg.KEYDOWN:
                if evento.key == K_LEFT:
                    nave.rect.left -= nave.velocidad
                elif evento.key == K_RIGHT:
                    nave.rect.right += nave.velocidad
                elif evento.key == K_SPACE:
                    x, y = nave.rect.center
                    nave.disparar(x,y)

        pg.display.update()

#Llamada a la función principal
cargarFondo()