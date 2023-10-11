import pygame as pg

class Asteroide(pg.sprite.Sprite):
    #Constructor que recibe las posiciones en X y Y
    def __init__(self, posX, posY):
        pg.sprite.Sprite.__init__(self)
        self.imagenAsteroide = pg.image.load("imagenes/asteroide.png")
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 4
        self.rect.top = posY
        self.rect.left = posX
        self.listaAsteroide = []

    #Metodo para visualizar el recorrido del meteorito
    def recorrido(self):
        self.rect.top = self.rect.top + self.velocidad

    #Metodo para visualizar el meteorito en pantalla
    def visualizarMeteorito(self, superficie):
        superficie.blit(self.imagenAsteroide, self.rect)