import cv2


#
imagen=cv2.imread("figuras_geometricas_prueba.jpg")
imagenEscalaGrises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_ , imagenEnUmbral = cv2.threshold(imagenEscalaGrises,210,255,cv2.THRESH_BINARY)
contorno, jerarquia = cv2.findContours(imagenEnUmbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contorno, -1, (100,100,100), 3)

#mostrar
cv2.imshow("imagen a color",imagen)
cv2.imshow("Imagen en escala de grises", imagenEscalaGrises)
cv2.imshow("Imgaen umbral", imagenEnUmbral)

cv2.waitKey(0)
cv2.destroyAllWindows()