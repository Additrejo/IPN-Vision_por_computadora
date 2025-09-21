# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 03:00:09 2022

@author: Addi.T for computer Visión. I.C.E, Instituto Politecnico Nacional
"""

import cv2
imagen = cv2.imread("C:\\Users\\addi_\\OneDrive\\Escritorio\\imagen1.jpg")


flip0 = cv2.flip(imagen,0)
cv2.imshow('Espejo vertical',flip0)
cv2.waitKey(0)