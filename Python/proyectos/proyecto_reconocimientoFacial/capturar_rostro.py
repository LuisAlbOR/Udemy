import cv2 as cv
import os
import imutils

modelo = 'Guicho'
rutaUno = 'E:/proyectos/proyectos_python/proyecto_reconocimientoFacial'
rutaCompleta = rutaUno + '/' + modelo

if not os.path.exists(rutaCompleta):
    os.makedirs(rutaCompleta)

camara = cv.VideoCapture(rutaUno + '\guicho.mp4') #para capturar rostros de videos solo pon la ruta del mp4 y nombre o solo el nombre ssi esta en la misma carpeta
ruido = cv.CascadeClassifier( 'E:\proyectos\proyectos_python\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
#print(ruido)
id = 1001

if not camara.isOpened():
    print("no se encontro una camara")

while True:
    respuesta , videoCamara = camara.read()
    
    if respuesta == False:
        break

    #videoCamara = imutils.resize(videoCamara, width=640)
    videoEscalaGrises = cv.cvtColor(videoCamara, cv.COLOR_BGR2GRAY)
    idCaptura = videoCamara.copy()
    reconocerCara = ruido.detectMultiScale(videoEscalaGrises, 1.2, 2)

    for (x, y, e1, e2) in reconocerCara:
        cv.rectangle(videoCamara, ( x , y ), ( x+e1 , y+e2 ), (255,255,255), 2)
        rostroCapturado = idCaptura[y:y+e2, x:x+e1]
        rostroCapturado = cv.resize(rostroCapturado, (160,160), interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutaCompleta + '/imagen_{}.jpg'.format(id), rostroCapturado)
        id=id+1

    cv.imshow("Resultado del reconocimiento", videoCamara)
    
    if id == 2001:
        break

    if cv.waitKey(1) == ord("m"):
        break

camara.release()
cv.destroyAllWindows()