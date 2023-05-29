import cv2 as cv
import os
import imutils

dataRuta = 'E:/proyectos/proyectos_python/proyecto_reconocimientoFacial/data'
listaData = os.listdir(dataRuta)

entrenamientoEigenRecognizer = cv.face.EigenFaceRecognizer_create()

entrenamientoEigenRecognizer.read('E:/proyectos/proyectos_python/proyecto_reconocimientoFacial/Entrenamiento_EigenRecognize.xml')

ruido = cv.CascadeClassifier( 'E:\proyectos\proyectos_python\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')

camara = cv.VideoCapture(1)

while True:
    respuesta , videoCamara = camara.read()

    if respuesta == False: break
    videoCamara = imutils.resize(videoCamara, width=640)

    videoEscalaGrises = cv.cvtColor(videoCamara, cv.COLOR_BGR2GRAY)
    idCaptura = videoEscalaGrises.copy()
    reconocerCara = ruido.detectMultiScale(videoEscalaGrises, 1.3, 5)

    for (x, y, e1, e2) in reconocerCara:

        rostroCapturado = idCaptura[y:y+e2, x:x+e1]
        rostroCapturado = cv.resize(rostroCapturado, (160,160), interpolation=cv.INTER_CUBIC)
        resultado = entrenamientoEigenRecognizer.predict(rostroCapturado)
        cv.putText( videoCamara , '{}'.format(resultado) , (x , y-5), 1, 1.3, (0,255,0), 1, lineType=cv.LINE_AA)
        
        if resultado[1] < 9000:
            cv.putText( videoCamara , '{}'.format(listaData[resultado[0]]) , (x , y-22), 2, 1.1 , (0,255,0), 1, lineType=cv.LINE_AA)
            cv.rectangle(videoCamara, (x,y), (x+e1, y+e2), (255,0,0), 2) 
        else:
            cv.putText( videoCamara ,"No encontrado" , (x , y-22), 2, 0.7, (0,255,0), 1, lineType=cv.LINE_AA)
            cv.rectangle(videoCamara, (x,y), (x+e1, y+e2), (255,0,0), 2) 
            

    cv.imshow("Resultados", videoCamara)

    if cv.waitKey(1) == ord('m'):
        break

camara.release()
cv.destroyAllWindows()