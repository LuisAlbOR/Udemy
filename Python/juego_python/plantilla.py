import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Titulo de la ventana")
colorFondo = (100,150,70)

while True:
    ventana.fill(color=colorFondo)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit
        pygame.display.update()