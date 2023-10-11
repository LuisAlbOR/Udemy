import pygame as pg
#Importar desde clases

from clases import disparo


class Nave(pg.sprite.Sprite):
    #Metodo constructor
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.imagenNave = pg.image.load("imagenes/nave.png")
        self.imagenNaveExplota = pg.image.load("imagenes/naveExplota.png")

        #Tomamos el rectangulo de la imagen nave
        self.rect = self.imagenNave.get_rect()

        #Posicion inicial de la nave
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocidad = 20
        self.vida = True
        self.listaDisparo = []

        #Sonidos de la nave
        self.sonidoDisparo = pg.mixer.Sound("sonidos/disparo.aiff")


    #Metodo para verificar que la nave se mueve dentro de la ventana
    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 490:
                self.rect.right = 490

    #Metodo para disparar
    def disparar(self, x, y):
        if self.vida == True:
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()

    #Metodo para visualizar la nave en la pantalla
    def visualizarJugador(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenNaveExplota, self.rect)