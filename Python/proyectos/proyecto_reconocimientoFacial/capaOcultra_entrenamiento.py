import cv2 as cv
import os
import numpy as np
from time import time 


dataRuta = 'E:/proyectos/proyectos_python/proyecto_reconocimientoFacial/data'
listaData = os.listdir(dataRuta)
#print('titulo', listaData)
ids = []
rostrosData = []
id = 0
tiempoInicial = time()

for fila in listaData:
    rutaCompleta = dataRuta + '/' + fila

    print("Iniciando lectura...")
    for archivo in os.listdir(rutaCompleta):
        print('Imagenes: ', fila + '/' + archivo)
        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta + '/' + archivo, 0))
        #imagenes = cv.imread(rutaCompleta + '/' + archivo, 0)
    
    id = id + 1
    tiempoFinalLectura = time()
    tiempoTotalLectura = tiempoFinalLectura - tiempoInicial
    print('Tiempo total de lectura: ', tiempoTotalLectura)

entrenamientoEigenRecognizer = cv.face.EigenFaceRecognizer_create()

print("Iniciando el entrenamiento... Por favor, espere")
entrenamientoEigenRecognizer.train(rostrosData, np.array(ids))

tiemporFinalEntrenamiento = time()
tiempoTotalEntrenamiento = tiemporFinalEntrenamiento -tiempoTotalLectura
print('Tiempor de entrenamiento total: ', tiempoTotalEntrenamiento)

entrenamientoEigenRecognizer.write( 'E:/proyectos/proyectos_python/proyecto_reconocimientoFacial/Entrenamiento_EigenRecognize.xml')
print("Entrenamiento concluido")