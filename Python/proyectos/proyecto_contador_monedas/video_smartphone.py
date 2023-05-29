import cv2 as cv #Se renombra  la importación para mejor entendimiento

capturaVideo = cv.VideoCapture(1) #se obtiene de la PC la camara que se usa

if not capturaVideo.isOpened():
    print("No se  encontro una cámara")
    exit()

while True:
    tipoCamara, videoCamara = capturaVideo.read() #Leemos la variable que contiene la  camara para poder mostrarla
    videoEscalaGrises = cv.cvtColor(videoCamara, cv.COLOR_BGR2GRAY)
    
    cv.imshow("En vivo", videoEscalaGrises)

    if cv.waitKey(1) == ord("q"):
        break

capturaVideo.release()
cv.destroyAllWindows()