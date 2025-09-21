"""
Created on Thu Dec 29 22:20:58 2022
@author: Addi.T for computer Visión. I.C.E, Instituto Politecnico Nacional
"""

import cv2
import numpy as np

image = cv2.imread('C:\\Users\\addi_\\OneDrive\\Escritorio\\imagen1.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),90,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen Transpuesta, By: Addi Trejo',imageOut)
cv2.waitKey(0)
cv2.destroyAllWindows()