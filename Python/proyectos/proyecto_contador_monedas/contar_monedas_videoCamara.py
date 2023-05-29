import cv2
import numpy as np

def ordenarPuntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()

    y_order = sorted( n_puntos, key=lambda n_puntos:n_puntos[1])

    x1_order = y_order[:2]
    x1_order = sorted( x1_order, key=lambda x1_order:x1_order[0])

    x2_order = y_order[2:4]
    x2_order = sorted( x2_order, key=lambda x2_order:x2_order[0])

    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alineamientoVideo(imagen, ancho, alto):
    imagenAlineada = None
    videoEscalaGrises = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
    tipoUmbral, imagenUmbral = cv2.threshold(videoEscalaGrises, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("Video en Umbral" , imagenUmbral)

    contorno = cv2.findContours( imagenUmbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    contorno  = sorted(contorno, key=cv2.contourArea, reverse=True)[:1]

    for c in contorno:
        epsilon = 0.01 * cv2.arcLength( c, True)

        aproximacion = cv2.approxPolyDP( c, epsilon, True)

        if len(aproximacion) == 4:
            puntos = ordenarPuntos(aproximacion)
            puntoS1 = np.float32(puntos)
            puntoS2 = np.float32([[0,0], [ancho,0], [0,alto], [ancho, alto]])

            M = cv2.getPerspectiveTransform( puntoS1, puntoS2)
            imagenAlineada = cv2.warpPerspective( imagen, M, (ancho, alto) )
    
    return imagenAlineada

capturaVideo = cv2.VideoCapture(1)

if not capturaVideo.isOpened():
    print("No se  encontro una cámara")
    exit()

while True:
    tipoCamara, videoCamara = capturaVideo.read()

    if tipoCamara == False:
        break

    imagen_A4 = alineamientoVideo( videoCamara, ancho=480, alto=640)

    if imagen_A4 is not None:
        puntos = []
        valorMatrizGauss = 5

        videoEscalaGrises2 = cv2.cvtColor( imagen_A4, cv2.COLOR_RGB2GRAY)

        videoFiltroGaussiano = cv2.GaussianBlur( videoEscalaGrises2, (valorMatrizGauss,valorMatrizGauss), 1)

        tipoUmbral , videoUmbral = cv2.threshold( videoFiltroGaussiano, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

        cv2.imshow("Video en Umbral", videoUmbral)

        contorno2=cv2.findContours(videoUmbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        cv2.drawContours( image=imagen_A4 , contours=contorno2 , contourIdx=-1 , color=(0,0,255))

        sumaUnPeso = 0.0 #suma de el valor de cada moneda

        for c in contorno2:
            areaMoneda = cv2.contourArea(c)

            momentos = cv2.moments(c)

            if (momentos["m00"] == 0):
                momentos["m00"] = 1.0
    
            x = int(momentos["m10"] / momentos["m00"])
            y = int(momentos["m01"] / momentos["m00"])

            if areaMoneda < 10600 and areaMoneda > 9000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText( imagen_A4, "$/. 1.00", (x,y), font, 0.65, (0,255,0), 2)

                sumaUnPeso = sumaUnPeso + 1

        total = sumaUnPeso
        print("Sumatoria total de monedas de un peso: ", round(total,2))
        cv2.imshow("Imagen en A6", imagen_A4)
        cv2.imshow("Camara", videoCamara)

    if cv2.waitKey(1) == ord('m'):
        break

capturaVideo.release()
cv2.destroyAllWindows()