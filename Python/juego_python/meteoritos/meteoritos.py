import pygame as pg
import sys
from pygame.locals import *
#Importando nuestras clases
from clases import jugador
from clases import asteroide
from random import randint
import time

#Declaración de variables
ancho = 480
alto = 700
listaAsteroide = []
puntos = 0
colorFuente = (255,255,255)

#Boolean para ver si se puede jugar
jugando = True

#Cargar asteorides
def cargarAsteroides(x,y):
    meteorito = asteroide.Asteroide(x,y)
    listaAsteroide.append(meteorito)

def gameOver():
    global jugando
    jugando = False
    for meteoritos in listaAsteroide:
        listaAsteroide.remove(meteoritos)

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

    #Contador
    contador = 0

    #Cargar los sonidos de fondo
    pg.mixer.music.load("sonidos/fondo.wav")
    pg.mixer.music.play(3)
    sonidoColision = pg.mixer.Sound("sonidos/colision.aiff")

    global puntos

    #Fuentes de texto
    fuenteMarcador = pg.font.SysFont("Verdana", 30)


    #Ciclo de juego
    while True:

        ventana.blit(fondo, (0, 0))
        nave.visualizarJugador(ventana)

        #Tiempo
        tiempo = time.time()

        #Marcador
        textoMarcador = fuenteMarcador.render("Punto : " + str(puntos), 0, colorFuente)
        ventana.blit(textoMarcador, (0, 0))
        #Creamos asteroides
        if tiempo - contador > 1:
            contador = tiempo
            posX = randint(2,460)
            cargarAsteroides(posX,0)

        #Comprobamos la lista asteroides
        if len(listaAsteroide) > 0:
            for x in listaAsteroide:
                if jugando == True:
                    x.visualizarMeteorito(ventana)
                    x.recorrido()
                if x.rect.top > 700:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaAsteroide.remove(x)
                        sonidoColision.play()
                        nave.vida = False
                        gameOver()
                        #print("colision nave / meteorito")

        #Verificar el disparo
        if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:
                x.visualizarDisparo(ventana)
                x.recorrido()
                if x.rect.top <- 10:
                    nave.listaDisparo.remove(x)
                else:
                    for meteoritos in listaAsteroide:
                        if x.rect.colliderect(meteoritos.rect):
                            listaAsteroide.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntos += 1
                            print("colision disparo / meteorito")
        nave.mover()

        #Eventos principales
        for evento in pg.event.get():
            if evento.type == QUIT:
                pg.quit()
                sys.exit()
            elif evento.type == pg.KEYDOWN:
                if jugando == True:
                    if evento.key == K_LEFT:
                        nave.rect.left -= nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right += nave.velocidad
                    elif evento.key == K_SPACE:
                        x, y = nave.rect.center
                        nave.disparar(x,y)

        if jugando == False:
            fuenteGameOver = pg.font.SysFont("Verdana", 40)
            textoGameOver = fuenteGameOver.render("GAME OVER", 0, colorFuente)
            ventana.blit(textoGameOver, ( 140, 350))
        pg.mixer.music.fadeout(3000)
        pg.display.update()

#Llamada a la función principal
cargarFondo()