import cv2
import numpy as np


imagen = cv2.imread('C:\\Users\\addi_\\OneDrive\\Escritorio\\Lunarcrater5.jpeg')
cv2.imshow("Original",imagen)
height, width = imagen.shape[0:2]



def iD(): 
    imgI=[[0 for i in range(width)]for j in range(height)]
    for i in range(height):
      for j in range(width):
        imgI[i][j]=imagen[i][j]
    imgI=np.uint8(imgI)
    cv2.imshow("Identidad",imgI)
    
############################################################

def iN(): 
    imgN=[[0 for i in range(width)]for j in range(height)]
    for i in range(height):
        for j in range(width):
            inverso=np.array(imagen[i][j])
            imgN[i][j]=255-inverso
    imgN=np.uint8(imgN)
    cv2.imshow("Inverso Negativo",imgN)
############################################################


def iU():
    imgU=[[0 for i in range(width)]for j in range(height)]
    p1=40      #La visualización de la imagen es proporcional a p1 y p2
    p2=110
    for i in range(height):
        for j in range(width):
            if (imagen[i][j][1]<=p1 or imagen[i][j][1] >=p2):
                imgU[i][j]=255
            else:
                imgU[i][j]=0
    imgU=np.uint8(imgU)
    cv2.imshow("Umbral",imgU)
############################################################


def iUB():
    imgUB=[[0 for i in range(width)]for j in range(height)]
    p1=40      #La visualización de la imagen es proporcional a p1 y p2
    p2=110
    for i in range(height):
       for j in range(width):
           if (imagen[i][j][1] < p1 or imagen[i][j][1] >=p2):
               imgUB[i][j]=255
           else:
               imgUB[i][j]=0
    imgUB=np.uint8(imgUB)
    cv2.imshow("Umbral binario",imgUB)


############################################################

def iUBI():
    imgBI=[[0 for i in range(width)]for j in range(height)]
    p1=40       #La visualización de la imagen es proporcional a p1 y p2
    p2=110
    for i in range(height):
        for j in range(width):
            if (imagen[i][j][1] <= p1 or imagen[i][j][1]>=p2):
                imgBI[i][j]=0
            else:
                imgBI[i][j]=255
    imgBI=np.uint8(imgBI)
    cv2.imshow("Umbral binario invertido",imgBI)


############################################################

def iUEG(): 
    imgUEG=[[0 for i in range(width)]for j in range(height)]
    P1=40
    P2=110
    for i in range(height):
        for j in range(width):
            if (imagen[i][j][1] <= P1 or imagen[i][j][1] >=P2):
                imgUEG[i][j]=255
            else:
                imgUEG[i][j]=imagen[i][j][1]
    imgUEG=np.uint8(imgUEG)
    cv2.imshow("umbral escala de grises", imgUEG)

############################################################

def iUIEGI():
    imgUEGI=[[0 for i in range(width)]for j in range(height)]
    P1=40
    P2=110
    for i in range(height):
        for j in range(width):
            if (imagen[i][j][1] <= P1 or imagen[i][j][1] >=P2):
                imgUEGI[i][j]=255
            else:
                imgUEGI=255-imagen   
    imgUEGI=np.uint8(imgUEGI)
    cv2.imshow("Umbral escala grises Invertido", imgUEGI)

############################################################

iD()
iN()
iU()
iUB()
iUBI()
iUEG()
iUIEGI()
cv2.waitKey(0)
cv2.destroyAllWindows()