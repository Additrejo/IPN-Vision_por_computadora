# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:04:23 2022

@author: Addi.T for computer Visión. I.C.E, Instituto Politecnico Nacional
"""

import cv2

imagen = cv2.imread('C:\\Users\\addi_\\OneDrive\\Escritorio\\imagen1.jpg')
flip_1 = cv2.flip(imagen,1)

cv2.imshow('Espejo Horizontal, By:Addi Trejo',flip_1)
cv2.waitKey(0)