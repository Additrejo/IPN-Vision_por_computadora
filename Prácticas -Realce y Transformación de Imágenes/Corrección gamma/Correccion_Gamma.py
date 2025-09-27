import cv2
import numpy as np
import math
img = cv2.imread('C:\\Users\\addi_\\OneDrive\\Escritorio\\sinus_iridium.jpg')
   
def funLog(imagen):
    imagen=np.float32(imagen)
    B, G, R = cv2.split(imagen)
    al = 1
    BP=(255/np.log(al*255+1))*np.log(al*B+1)
    GP=(255/np.log(al*255+1))*np.log(al*G+1)
    RP=(255/np.log(al*255+1))*np.log(al*R+1)
    union = cv2.merge([BP,GP,RP])
    union=np.uint8(union)
    cv2.imwrite("Logaritmica.jpg", union)
    union = cv2.cvtColor(union,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Logaritmica", union)
   

def funSen(imagen):
    imagen=np.float32(imagen)
    B, G, R = cv2.split(imagen)
    BP=255*np.sin(((math.pi)*B)/(2*255))
    GP=255*np.sin(((math.pi)*G)/(2*255))
    RP=255*np.sin(((math.pi)*R)/(2*255))
    union = cv2.merge([BP,GP,RP])
    union=np.uint8(union)
    cv2.imwrite("Senoidal.jpg", union)
    union = cv2.cvtColor(union,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Senoidal", union)
  


def funExp(imagen):
    gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Escala de Grises",gray)
    imagen=np.float32(imagen)
    B, G, R = cv2.split(imagen)
    ae = -10
    BP=(255/(1-(math.e**(ae))))*(1-math.e**((ae*B)/255))
    GP=(255/(1-(math.e**(ae))))*(1-math.e**((ae*G)/255))
    RP=(255/(1-(math.e**(ae))))*(1-math.e**((ae*R)/255))
    union = cv2.merge([BP,GP,RP])
    union=np.uint8(union)
    cv2.imwrite("Exponencial.jpg", union)
    union = cv2.cvtColor(union,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Exponencial", union)
    

def funCos(imagen):
    gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Escala de Grises",gray)
    imagen=np.float32(imagen)
    height, width = imagen.shape[0:2]
    imagenAux=[[0 for i in range(width)]for j in range(height)]
    for i in range(height):
        for j in range(width):
            imagenAux[i][j]=255*(1-(np.cos((np.pi*(imagen[i,j]))/(2*255))))
    union=np.uint8(imagenAux)
    cv2.imwrite("Cosenoidal.jpg", union)
    union = cv2.cvtColor(union,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Cosenoidal", union)
    

    
def funExpCres(imagen):
    gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Escala de Grises",gray)
    imagen=np.float32(imagen)
    height, width = imagen.shape[0:2]
    imagenAux=[[0 for i in range(width)]for j in range(height)]
    aec = 2
    constante=(255/((np.e**aec)-1))
    for i in range(height):
        for j in range(width):
            imagenAux[i][j]=constante*(np.e**((aec*(imagen[i,j]))/255)-1)
    union=np.uint8(imagenAux)
    cv2.imwrite("Exponencial_Creciente.jpg", union)
    union = cv2.cvtColor(union,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Exponencial Creciente", union)
  


funLog(img)
funSen(img)
funExp(img)
funCos(img)
funExpCres(img)
cv2.waitKey(0)
cv2.destroyAllWindows()