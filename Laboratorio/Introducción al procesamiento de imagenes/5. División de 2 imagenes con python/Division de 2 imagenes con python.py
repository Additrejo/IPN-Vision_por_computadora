# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 02:55:42 2022

@author: Addi T. for computer Vision. I.C.E, Instituto Politecnico Nacional
"""

import cv2 
import numpy as np

imagen=cv2.imread("C:\\Users\\addi_\\OneDrive\\Escritorio\\imagen1.jpg")
cv2.imshow("Imagen original",imagen)

imagen1=cv2.imread("C:\\Users\\addi_\\OneDrive\\Escritorio\\imagen2.jpg")
cv2.imshow("Imagen original1",imagen1)

f=imagen.shape
f1=imagen1.shape

print("la primera dimension m es", f[0])
print("la segunda dimension n es", f[1])
print("la tercera dimension l es", f[2])

print("la primera dimension m es", f1[0])
print("la segunda dimension n es", f1[1])
print("la tercera dimension l es", f1[2])

nueva=np.zeros([f[0],f[1],f[2]],dtype=np.uint8)
nueva1=np.zeros([f1[0],f1[1],f1[2]],dtype=np.uint8)

for x in range(f[0]):
    for y in range(f[1]):
        for z in range(f[2]):
            
            nueva[x,y,z] = imagen1[x,y,z]/imagen[x,y,z]
            nueva1[x,y,z] = (imagen1[x,y,z]/imagen[x,y,z])/2
            

            
cv2.imshow("Division de 2 imagenes, By: Addi Trejo",nueva)            


cv2.waitKey(0)
cv2.destroyAllWindows()
