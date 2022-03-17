import numpy as np
import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50)

while (True):
    
    ret, frame = cap.read() # Capturamos una imagen a la vez
    parameters = aruco.DetectorParameters_create()
    marker_corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    if ids != ids.any(None):
        print(f'ids detectados: {ids}')
        #print(f'marker_corners: {marker_corners[0]}')
    #print(f'rejectedImgPoints: {rejectedImgPoints}')

    frame = aruco.drawDetectedMarkers(frame, marker_corners)

    
    cv2.imshow('frame', frame) # Mostramos en la imagen los ArUcos encontrados
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release() # Liberamos la cámara al final de la utilización 
cv2.destroyAllWindows()