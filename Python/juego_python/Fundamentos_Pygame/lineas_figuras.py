import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((600,400))
pygame.display.set_caption("Titulo de la ventana")
#Colores
colorFondo = (100,150,70)
colorLinea = (255,120,0)
colorCirculo = (200,109,20)
colorFiguras = (105,220,185)

while True:
    ventana.fill(color=colorFondo)
    #Dibujando lineas
    pygame.draw.line(ventana,colorLinea, (10,10), (100,100),5)
    pygame.draw.line(ventana,colorLinea, (100,100), (100,200), 5)

    #Dibujando circulos
    pygame.draw.circle(ventana, colorCirculo, (200,50), 50, 5)
    pygame.draw.circle(ventana, colorCirculo, (300,50), 50, 5)

    #Dibujar figuras
    pygame.draw.rect(ventana, colorFiguras, (200,100,200,100))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()