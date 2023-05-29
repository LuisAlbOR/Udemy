import cv2 as cv #renombramos el cv2 para que sea mas facil identificar o usar

#extraemos el archivo que identifica el rostro e ignora los objetos extraños (ruidos)
ruido = cv.CascadeClassifier( 'E:\proyectos\proyectos_python\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
#la direccion del archivo depende de cdonde descomrimes el archivo de openCV
#print(ruido)

camara = cv.VideoCapture(0) #obtenemos el tipo de camara para obtener los rostros

if not camara.isOpened(): #verificamos que se haya obtenido correctamente la camara
    print("no se encontro una camara")
    exit()

while True: #si es verdad que se obtuvo una camara hara lo siguinte
    _ , videoCamara = camara.read() #leemos la camara para poder obtener el video  
    videoEscalaGrises = cv.cvtColor(videoCamara, cv.COLOR_BGR2GRAY) #pasamos el video que esta en colores a B/N
    reconocerCara = ruido.detectMultiScale(videoEscalaGrises, 1.2, 2) #obtenemos en una variable el reconocimiento del rostro(explicar presencialmente)

    for (x, y, e1, e2) in reconocerCara: #un ciclo que lee cada frame del video(explicar presencialmente)
        cv.rectangle(videoCamara, ( x , y ), ( x+e1 , y+e2 ), (255,255,255), 2) #dibujamos un contorno en la ubicacion del rostro
    
    cv.imshow("Resultado del reconocimiento", videoCamara) #mostramos la camara con la camara con el contorno
    
    if cv.waitKey(1) == ord("m"): #verificamos la salida del video
        break

camara.release() #cerramos la camara
cv.destroyAllWindows() #destruimos todas las ventanas con las telcas de direccion