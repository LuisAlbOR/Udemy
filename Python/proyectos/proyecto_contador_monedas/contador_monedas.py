import cv2
import numpy as np

valorGauss = 11
valorKernel = 5

imagenOriginal = cv2.imread("monedascontorno/monedas.jpg") #Obtenemos la imagen original para su manipulación

imagenEscalaGrises = cv2.cvtColor(imagenOriginal, cv2.COLOR_BGR2GRAY) #Pasamos la imagen original a B/N simple

imagenGauss = cv2.GaussianBlur(imagenEscalaGrises, (valorGauss, valorGauss), 0) #La imagen en escala de grises le metemos un desenfoque Gaussiano

imagenCanny = cv2.Canny(imagenGauss, 50, 100) #De la imagen con desenfoque obtenemos los bordes de cada objeto de la imagen

imagenKernel = np.ones((valorKernel,valorKernel), np.uint8) #Creamos un kernel (te lo explicare presencial) de una matriz y la pasamos a 8 bits

imagenCierre = cv2.morphologyEx(imagenCanny, cv2.MORPH_CLOSE, imagenKernel) #Pasamos la imagen en Canny y eliminamos el ruido interno(bordes internos que no nos sirven)

contornos, jerarquia = cv2.findContours(imagenCierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Encontramos los contornos de cada objeto de la imagen sin ruido interno

print("Monedas encontradas: {}".format(len(contornos)) ) #imprimimos en terminal la cantidad de contornos encontrados

cv2.drawContours(imagenOriginal, contornos, -1, (0, 0, 255), 2) #Dibujamos todos los contornos encontrados en la imagen original  de color rojo

#mostrar resultados

cv2.imshow("Imagen en escala de grises", imagenEscalaGrises)
cv2.imshow("Imagen con desenfoque Gaussiano", imagenGauss)
cv2.imshow("Imagen en modo Canny", imagenCanny)
cv2.imshow("Imagen sin ruido interno", imagenCierre)
cv2.imshow("Resultado: ", imagenOriginal)
cv2.waitKey(0)